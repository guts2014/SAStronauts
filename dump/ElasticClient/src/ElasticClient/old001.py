import test2
from datetime import datetime
from elasticsearch import Elasticsearch
from pydoc import describe
from aifc import data
es = Elasticsearch()

def createdoc(year, city, specificity, tergroup):
    return {
            "year": year,
            "location":
            {
                "city": city,
                "specificity": specificity
                
            },
            "group": tergroup
}
    
def fuzzylikethisquery(like_this_string):
    returningstring = ""
    querybody = {
                 "query":
                 {
                  "fuzzy_like_this":
                  {
                   "fields": "group",
                   "like_text": like_this_string
                   },
                  "lenient": True
                  }
                 }
    result = es.search(index="terrorist", body=querybody)
    if( result['hits']['total'] > 0 ):
        returningstring += "Got %d Hits on City:\n" % result['hits']['total']
        for hit in result['hits']['hits']:
            returningstring += "%(year)s %(location)s: %(group)s\n" % hit["_source"]
    else:
        returningstring = str(False)

def searchonallterrorstrings(querytype, querystring):
    returningstring = ""    
    
    querybody = {
            "query":
            {
                querytype: {"city": querystring},
            }
    } 
    result = es.search(index="terrorist", body=querybody)
    if( result['hits']['total'] > 0 ):
        returningstring += "Got %d Hits on City:\n" % result['hits']['total']
        for hit in result['hits']['hits']:
            returningstring += "%(year)s %(location)s: %(group)s\n" % hit["_source"]
        returningstring += "\n\n"
     
    querybody = {
            "query":
            {
                querytype: {"group": querystring},
            }
    } 
     
    result = es.search(index="terrorist", body=querybody)
    if( result['hits']['total'] > 0 ):
        returningstring += "Got %d Hits on Group:\n" % result['hits']['total']
        for hit in result['hits']['hits']:
            returningstring += "%(year)s %(location)s: %(group)s\n" % hit["_source"]
    
    return returningstring

def searchonallterrorstrings2(querytype, querystring):
    returningstring = ""    
    
    querybody = {
            "query":
            {
                querytype: {"_all": querystring},
            }
    } 
    result = es.search(index="terrorist", body=querybody)
    if( result['hits']['total'] > 0 ):
        returningstring += "Got %d Hits:\n" % result['hits']['total']
        for hit in result['hits']['hits']:
            returningstring += "%s\n" % hit["_source"] # "%(year)s %(location)s: %(group)s\n" % hit["_source"]
        returningstring += "\n\n"
    return returningstring


# res = es.index(index="terrorist", doc_type="incident", body=doc)
#res = es.index(index="terrorist", doc_type="incident", body=createdoc(2001, "new york", 1, "al-quaeda"))

#res = es.get(index="terrorist", doc_type='incident', id=1)
#print(res['_source'])

#es.indices.refresh(index="terrorist")

#===============================================================================
# fuzzyquery = {
#                 "query":
#                 {
#                     "fuzzy": {"city": "glasgow"}
#                 }
# }
# 
# queryresult = searchonallterrorstrings2("fuzzy", "alquaeda")
# print (queryresult)
#===============================================================================

def getdata(date_year=1970,date_month=0,date_day=0,date_approxdate="",date_extend_val="",date_extend_date="",
loc_country="",loc_region="",loc_state="",loc_city="",loc_spec="",loc_vicinity="",loc_details="",
loc_coord_lat="",loc_coord_long="",summary="",criterion_c1="",criterion_c2="",criterion_c2="",
criterion_doubtterr="",alternative="",multiple="",success="",suicide="",attacktype="",target_atktype="",target_corp="",target_natio="",groupname="",groupsubname="",motive="",groupconfirmed="",perpetrators="",perpetratorscaptured="",claimed="",wep_type="",wep_subtype="",wep_detail="",kills="",wounds="",
propertydmg="",hostages="",ransom="",note="",sources="",related=""):
    return {
    "data":
    {
      "key":
      {
       "date":
        {
         "year": date_year, # type: int
         "month": date_month, # type: int
         "day": date_day, # type: int
         "approxdate": date_approxdate, # type: string
         "extend":
         {
            "val": date_extend_val, # type: string
            "date": date_extend_date # type: string
         } #end: extend
        }, #end: date
       "location":
       {
            "country": loc_country, # type: string
            "region": loc_region, # type: string
            "state": loc_state, # type: string
            "city": loc_city, # type: string
            "specificity": loc_spec, # type: string
            "vicinity": loc_vicinity, # type: string
            "locationDetails": loc_details, # type: string
            "coordinates":
            {
                "latitude": loc_coord_lat, # type: string
                "longitude": loc_coord_long # type: string
            } #end: coordinates 
        }, #end: location
        "summary": summary, # type: string
        "criterion":
        {
            "crit1": criterion_c1, # type: string
            "crit2": criterion_c2, # type: string
            "crit3": criterion_c2, # type: string
            "doubtterr": criterion_doubtterr # type: string
        }, #end: criterion
       "alternative": alternative, # type: string
       "multiple": multiple, # type: string # Multiple Attacks?
       "success": success, # type: string
       "suicide": suicide, # type: string
       "atacktype": attacktype, # type: string
       "target":
        {
            "atktype": target_atktype, # type: string
            "corporation": target_corp, # type: string
            "nationality": target_natio # type: string
        }, #end: target
        "group_name": groupname, # type: string
        "group_subname": groupsubname, # type: string
        "motive": motive, # type: string
        "group_confirmed": groupconfirmed, # type: string
        "perps": perpetrators, # type: string
        "perpsCaptured": perpetratorscaptured, # type: string
        "claimed": claimed, # type: string # Someone claimed the responsibility for the attack?
        "weapon":
        {
         "weptype": wep_type, # type: string
         "wepsubtype": wep_subtype, # type: string
         "details": wep_detail # type: string
         }, #end: weapon
         "kills": kills, # type: string
         "wounds": wounds, # type: string
         "propertydmg": propertydmg, # type: string
         "hostages": hostages, # type: string
         "ransom": ransom, # type: string
         "note": note, # type: string
         "sources": sources, # type: string
         "related": related # type: string
         } #end: key
     } #end: data
            } #end: returning dict

def getkey(id, year, month, day, approxdate="", extendval="",extenddate=""):
    return {
            "key":
            {
                "date":
                {
                    "START-ID": id,
                    "properties":
                    {
                        "year": year,
                        "month": month,
                        "day": day,
                        "approxdate": approxdate,
                        "extend":
                        {
                            "val": extendval,
                            "date": extenddate
                        }
                    }
                }
            }
        } #end

keytemplate = {
    "key":
    {
        "properties":
        {
                "date":
            {
                "START-ID": {"type": "string"},
                "properties":
                {
                    "year": {"type": "integer"},
                    "month": {"type": "integer"},
                    "day": {"type": "integer"},
                    "approxdate": {"type": "string"},
                    "extend":
                    {
                        "properties":
                        {
                            "val": {"type": "string"},
                            "date": {"type": "string"}
                        }
                    }
                }
            }
        }
    }
}

#res = es.index(index="terrorist", doc_type="key", id=1970000000000, body=getkey(id=1970000000000, year=1970, month=0, day=0, approxdate="20-30 January"))
#print(res['created'])


for idx in data:
    es.index(index="terrorist", doc_type="data", id = idx, body = getdata)
    
    
    
    
    
print (searchonallterrorstrings2("fuzzy", "1970"))


#res = es.search(index="terrorist", body=searchonallterrorstrings("fuzzy", "glasgow"))
#print("Got %d Hits:" % res['hits']['total'])
#for hit in res['hits']['hits']:
#    print("%(year)s %(location)s: %(group)s" % hit["_source"])