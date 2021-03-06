import test2
from elasticsearch import Elasticsearch
es = Elasticsearch() # [{"host": "54.68.249.254"}]
 
def searchonallterrorstrings(querytype, querystring):
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

def getdata(date_year=1970,date_month=0,date_day=0,date_approxdate="",date_extend_val="",date_extend_date="",
loc_country="",loc_region="",loc_state="",loc_city="",loc_spec="",loc_vicinity="",loc_details="",
loc_coord_lat="",loc_coord_long="",summary="",criterion_c1="",criterion_c2="",criterion_c3="",
criterion_doubtterr="",alternative="",multiple="",success="",suicide="",attacktype="",targetlist=[{'type': ["", "", ""], 'subtype': ["", "", ""], 'corporation': ["", "", ""], 'target': ["", "", ""], 'nationality': ["", "", ""]}],groupname="",groupsubname="",motive="",groupconfirmed="",perpetrators="",
perpetratorscaptured="",claimed="",wep_type="",wep_subtype="",wep_detail="",kills="",wounds="",propertydmg="",hostages="",ransom="",note="",sources="",related=""):
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
            "crit3": criterion_c3, # type: string
            "doubtterr": criterion_doubtterr # type: string
        }, #end: criterion
       "alternative": alternative, # type: string
       "multiple": multiple, # type: string # Multiple Attacks?
       "success": success, # type: string
       "suicide": suicide, # type: string
       "atacktype": attacktype, # type: string
       "target": targetlist, # type: list
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


def main():
    print("dummy")
    countingindex = 0
    for idx in test2.data:
        print("IDX = "+idx+"\tProcess Number: "+str(countingindex)+"\n")
        countingindex += 1
        es.index(index="terrorist", doc_type="data", id = idx, body = getdata(date_year = test2.data[idx]["date"]["year"],
                                                                              date_month = test2.data[idx]["date"]["month"],
                                                                              date_day = test2.data[idx]["date"]["day"],
                                                                              date_approxdate = test2.data[idx]["date"]["approxdate"],
                                                                              date_extend_val = test2.data[idx]["date"]["extend"]["val"],
                                                                              date_extend_date = test2.data[idx]["date"]["extend"]["date"],
                                                                              loc_country = test2.meaning["country"][ test2.data[idx]["location"]["country"] ],
                                                                              loc_region = test2.meaning["region"][test2.data[idx]["location"]["region"]],
                                                                              loc_state = test2.data[idx]["location"]["state"],
                                                                              loc_city = test2.data[idx]["location"]["city"],
                                                                              loc_spec = test2.data[idx]["location"]["specificity"],
                                                                              loc_vicinity = test2.data[idx]["location"]["vicinity"],
                                                                              loc_details = test2.data[idx]["location"]["locationDetails"],
                                                                              loc_coord_lat = test2.data[idx]["location"]["coordinates"]["latitude"],
                                                                              loc_coord_long = test2.data[idx]["location"]["coordinates"]["longitude"],
                                                                              summary = test2.data[idx]["summary"],
                                                                              criterion_c1 = test2.data[idx]["criterion"]["crit1"],
                                                                              criterion_c2 = test2.data[idx]["criterion"]["crit2"],
                                                                              criterion_c3 = test2.data[idx]["criterion"]["crit3"],
                                                                              criterion_doubtterr = test2.data[idx]["criterion"]["doubtterr"],
                                                                              alternative = test2.meaning["alternative"][test2.data[idx]["alternative"]],
                                                                              multiple = test2.data[idx]["multiple"],
                                                                              success = test2.data[idx]["success"],
                                                                              suicide = test2.data[idx]["suicide"],
                                                                              attacktype = test2.data[idx]["atacktype"],
                                                                              targetlist = test2.data[idx]["target"],
                                                                              groupname = test2.data[idx]["group_name"],
                                                                              groupsubname = test2.data[idx]["group_subname"],
                                                                              motive = test2.data[idx]["motive"],
                                                                              groupconfirmed = test2.data[idx]["group_confirmed"],
                                                                              perpetrators = test2.data[idx]["perps"],
                                                                              perpetratorscaptured = test2.data[idx]["perpsCaptured"],
                                                                              claimed = test2.data[idx]["claimed"],
                                                                              wep_type = test2.data[idx]["weapon"]["type"],
                                                                              wep_subtype = test2.data[idx]["weapon"]["subtype"],
                                                                              wep_detail = test2.data[idx]["weapon"]["details"],
                                                                              kills = test2.data[idx]["kills"],
                                                                              wounds = test2.data[idx]["wounds"],
                                                                              propertydmg = test2.data[idx]["property"],
                                                                              hostages = test2.data[idx]["hostages"],
                                                                              ransom = test2.data[idx]["ransom"],
                                                                              note = test2.data[idx]["notes"],
                                                                              sources = test2.data[idx]["sources"],
                                                                              related = test2.data[idx]["related"]
                                                                              )
                 )
    print("redummy")
    
    
#main()