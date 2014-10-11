from elasticsearch import Elasticsearch
import string
from warnings import catch_warnings
es = Elasticsearch()


def getwhitespacecase(fields=["_all"],querystring=""):
    return {
            "query":
            {
                "fuzzy_like_this":
                {
                    "fields": fields,
                    "like_text" : querystring,
                }
            }
        } 

def getsinglewordcase(field="_all",querystring=""):
    return {
            "query":
            {
                "fuzzy": {field: querystring}
            }
    }

def query(searchstring="",maxresults=20,dbindex="terrorist",):
    print("Start of the function")
    if (' ' in searchstring):
        querybody = getwhitespacecase(querystring=searchstring)
    else:
        querybody = getsinglewordcase(querystring=searchstring)
    returninglist = []
    print("Before Query")
    result = es.search(index=dbindex,body=querybody)
    print("After Query")
    if(result['hits']['total'] <= 0):
        return "No Results"
    else:
        for querydata in result['hits']['hits']: # result['hits']['hits'] returns a list of dictionaries, querydata is the dictionary in the format of the JSON file returned by elasticsearch
            returningdict = { 
                                '_id': querydata['_id'],
                                '_score': querydata['_score'],
                                'coordinates': querydata['_source']['data']['key']['location']['coordinates'],
                                'city': querydata['_source']['data']['key']['location']['city'],
                                'state': querydata['_source']['data']['key']['location']['state'],
                                'country': querydata['_source']['data']['key']['location']['country'],
                                'region':  querydata['_source']['data']['key']['location']['region'],
                                'summary': querydata['_source']['data']['key']['summary']
                            }
            print(returningdict)
            returninglist = [returningdict] + returninglist
            if (len(returninglist)==maxresults):
                return returninglist
        return returninglist
    
def info(id_num="197000000000", datalist=["_all"],dbindex="terrorist",dbdoc="data"):
    result = es.get(index=dbindex, doc_type=dbdoc, id=id_num)
    if not (datalist == ["_all"]):
        keystocreate = []
        datatocreate = []
        for key1 in result.keys():
            print(1,key1)
            if type(result[key1]) is dict:
                for key2 in result[key1].keys():
                    print(2,key2)
                    if type(result[key1][key2]) is dict:
                        for key3 in result[key1][key2].keys():
                            print(3,key3)
                            if type(result[key1][key2][key3]) is dict:
                                for key4 in result[key1][key2][key3].keys():
                                    print(4,key4)
                                    if (key4 in datalist):
                                        print("Storing",key4,result[key1][key2][key3][key4])
                                        keystocreate.append(key4)
                                        datatocreate.append(result[key1][key2][key3][key4])
                            elif (key3 in datalist):
                                print("Storing",key3,result[key1][key2][key3])
                                keystocreate.append(key3)
                                datatocreate.append(result[key1][key2][key3])
                    elif (key2 in datalist):
                        print("Storing",key2,result[key1][key2])
                        keystocreate.append(key2)
                        datatocreate.append(result[key1][key2])
            elif (key1 in datalist):
                    print("Storing",key1,result[key1])
                    keystocreate.append(key1)
                    datatocreate.append(result[key1])
        print(keystocreate,datatocreate)
        returndict = {}
        for key,data in zip(keystocreate,datatocreate):
            returndict[key] = data
    return result