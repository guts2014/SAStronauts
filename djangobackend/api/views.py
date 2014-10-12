#from django.shortcuts import render
from django.http import HttpResponse
import queries, json

#This is a test view that returns the request to the server
def api_test(request):
    return HttpResponse("Your get request is: <br><br>"+str(request))

#this is a generic piece of text you will recieve if you go to /api/
def api_call(request):
    return HttpResponse("Hello. This is a generic api call. You want to be using <i><b>api/context/?q=hello</b></i> or <i><b>api/query/?q=hello</b></i>, bro!")

#this is a placeholder for the query view. the query view will return a bunch of json objects for all of the search results.
def api_query(request):
    q = request.GET.get('q', '')
    n = request.GET.get('n', 20)
    n = int(n)
    queryresults = queries.query(searchstring = q, maxresults=n)
    return HttpResponse(json.dumps(queryresults))

def api_info(request):
    data = json.loads(request.body)

    infodictionaries = {} #the list of json objects
    
    #iterating over the ids and getting the requested data on each
    for ids in data['ids']:
        infodictionaries[ids] = queries.info(id_num=ids, datalist=data['fields'])
    return HttpResponse(infodictionaries.dumps())#, content_type="application/json")
    

#this is a placeholder view for the context api call. This will return a json object with lots of good contextual data about the item requested.
def api_context(request):
    q = request.GET.get('q', '')
    return HttpResponse("<h1>Your context request was:</h1>" + q)




