import wikipedia
import urllib2
import json
import string
import random

# count how many times a kewyword appears on a website
def count(text, link, keywords):
    data = {}
    text = text.split()
    for kw in keywords:
        for word in text:
            if kw in word or kw.lower() in word:
                if data.has_key(kw):
                    data[kw] += 1
                else:
                    data[kw] = 1
    return [link, data]

def buildTitle(title):
    t = ''
    title = title.split()
    for word in title:
        t += word + '%20'
    t = t[:-3]
    return t

#
def getCount(keywords):
    total_data=[]
    kw_string = ''
    for kw in keywords:
        kw_string += kw + ' '

    results = []
    wikipedia.search(kw_string)

    for r in wikipedia.search(kw_string):
        results.append(r)

    for title in results:

        json_obj = urllib2.urlopen("http://en.wikipedia.org/w/api.php?action=query&titles=" +buildTitle(title)+ "&prop=info&format=json&inprop=protection%7Ctalkid")
        try:
            data = json.load(json_obj)
            pageid = data['query']['pages'].keys()[0]
            works = 1
        except:
            works = 0

        if works == 1:
            json_obj2 = urllib2.urlopen("http://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=json&pageids=" + pageid)
            data2 = json.load(json_obj2)
            data3 = data2['query']['pages'][pageid]['revisions'][0]['*'].encode('utf-8')
            dd = count(data3, title, keywords)
            total_data.append(dd)

    return total_data

def structureData(data):
    data_final = {}
    for d in data:
        link = 'http://en.wikipedia.org/wiki/' + buildTitle(d[0])
        data_final[link.encode('utf-8')] = d[1]
    return data_final


def getFields(keywords):
    field_values = {}
    for kw in keywords:
        field_values[keywords[kw]] = kw
    return field_values



def initializeData(keywords):
    keywords_only = []
    for kw in keywords:
        keywords_only.append(keywords[kw])
    return keywords_only

def getValue(field, keywords):
    fields = getFields(keywords)

    if fields[field] == 'Year':
        return 10
    if fields[field] == 'Month':
        return 6
    if fields[field] == 'Group':
        return 10
    if fields[field] == 'Target':
        return 10
    if fields[field] == 'Country':
        return 2
    if fields[field] == 'Region':
        return 6
    return 2




def getRelevantPages(data, keywords):
    scores = {}
    for link in data:
        scores[link] = 0
        for field in data[link]:
            score = getValue(field, keywords)*data[link][field]
            scores[link] += score
        print
    return scores

def getPercentages(data):
    percentages = {}
    total_score = 0
    for link in data:
        total_score += data[link]
    for link in data:
        percentage = (float(data[link])/float(total_score))*100
        percentages[link] = float('%.2f' % percentage)

    return percentages


def setupSearch(ElasticSearchKeywords):
    keywords = initializeData(ElasticSearchKeywords)
    data = getCount(keywords)
    scores = getRelevantPages(structureData(data),ElasticSearchKeywords)
    percentages = getPercentages(scores)
    return percentages

#example = {'Other1':'Military','Other2':'Army','Other3':'Police','Region':'Kokang','Year':'2009','Month':'September','Other5':'Shan State','Country':'Myanmar'})










