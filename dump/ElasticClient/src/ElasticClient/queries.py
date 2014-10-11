from elasticsearch import Elasticsearch
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
        returndict = {}
        returndict = findallnodesthatcontain(retdict=returndict, srchdict=result, dtlst=datalist)
        result = returndict
    return result

def findallnodesthatcontain(retdict,srchdict,dtlst=[],stacksize=0):
    newdict = retdict
    for key in srchdict.keys():
        if type(srchdict[key]) is dict:
            recursivedict = findallnodesthatcontain(retdict, srchdict[key],dtlst,stacksize+1)
            for things in recursivedict.keys():
                newdict[things] = recursivedict[things]
        elif (key in dtlst):
            newdict[key] = srchdict[key]
    return newdict 