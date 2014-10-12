import csv
import string

data = {}
meaning = {}
meaning['country'] = {"" : ""}
meaning['region'] = {"" : ""}
# meaning criterion
meaning['alternative'] = {"" : "", "1": "Insurgency/Guerilla Action", "2": "Other Crime Type", "3": "Intra/Inter-group Conflict", "4": "Lack of Intentionality", "5" : "State Actors"}
meaning['atack_type'] = {"": "", '1': 'Assassination', '2': 'Armed Assault', '3': 'Bombing/Explosion', '4': 'Hijacking', '5': 'Hostage Taking (Barricade Incident)',
                         '6': 'Hostage Taking (Kidnapping)', '7':'Facility/Infrastructure Attack', '8': 'Unarmed Assault', '9': 'Unknown'}
meaning['target_type'] = {"" : ""}
meaning['target_subtype'] = {"" : ""}
meaning['nationality'] = {"" : ""}
meaning['claim_mode'] = {"" : ""}
meaning['weapon_type'] = {"" : ""}
meaning['weapon_subtype'] = {"" : ""}
meaning['property'] = { "" : "", '1': 'Catastrophic (likely > $1 billion)', '2': 'Major (likely > $1 million but < $1 billion)',
                        '3': 'Minor (likely < $1 million)', '4': 'Unknown'}
meaning['hostages_outcome'] = {"" : ""}


org = {}


fields = []

def reader():
    with open('globalterrorismdb_0814dist.csv') as f:
        reader = csv.reader(f)
        i = True
        for row in reader:
            if i == True:
                for j in row:
                    fields.append(j)
            

            if i == False:
                key=row[0]
                data[key]={}
                data[key]['date']={}
                
                data[key]['date']['year'] = int(row[1])
                data[key]['date']['month'] = int(row[2])
                data[key]['date']['day'] = int(row[3])

                data[key]['date']['approxdate'] = row[4]
                data[key]['date']['extend'] = {}
                data[key]['date']['extend']['val'] = row[5]
                data[key]['date']['extend']['date'] = row[6]             #d/m/y

                data[key]['location'] = {}
                
                data[key]['location']['country'] = row[7]
                if row[7] not in meaning['country'].keys() and row[7]!= '':
                    meaning['country'][row[7]] = row[8]
                data[key]['location']['region'] = row[9]
                if row[9] not in meaning['region'].keys() and row[9]!= '':
                    meaning['region'][row[9]] = row[10]
                data[key]['location']['state'] = row[11]
                data[key]['location']['city'] = row[12]
                data[key]['location']['coordinates'] = {}
                data[key]['location']['coordinates']['latitude'] = row[13]
                data[key]['location']['coordinates']['longitude'] = row[14]
                data[key]['location']['specificity'] = row[15]
                data[key]['location']['vicinity'] = row[16]
                data[key]['location']['locationDetails'] = row[17]

                data[key]['summary'] = row[18]

                data[key]['criterion'] = {}
                data[key]['criterion']['crit1'] = row[19]
                data[key]['criterion']['crit2'] = row[20]
                data[key]['criterion']['crit3'] = row[21]
                data[key]['criterion']['doubtterr'] = row[22]

                data[key]['alternative'] = row[23]
                                           

                data[key]['multiple'] = row[25]
                data[key]['success'] = row[26]
                data[key]['suicide'] = row[27]

                data[key]['atacktype'] = [row[29], row[31], row[33]]

                            

                if row[34] not in meaning['target_type'].keys() and row[34] != '':
                    meaning['target_type'][row[34]] = row[35]
                if row[36] not in meaning['target_type'].keys() and row[36] != '':
                    meaning['target_subtype'][row[36]] = row[37]
                if row[40] not in meaning['nationality'].keys() and row[40] != '':
                    meaning['nationality'][row[40]] = row[41]
                if row[42] not in meaning['target_type'].keys() and row[42] != '':
                    meaning['target_type'][row[42]] = row[43]
                if row[44] not in meaning['target_type'].keys() and row[44] != '':
                    meaning['target_subtype'][row[44]] = row[45]
                if row[48] not in meaning['nationality'].keys() and row[48] != '':
                    meaning['nationality'][row[48]] = row[49]
                if row[50] not in meaning['target_type'].keys() and row[50] != '':
                    meaning['target_type'][row[50]] = row[51]
                if row[52] not in meaning['target_type'].keys() and row[52] != '':
                    meaning['target_subtype'][row[52]] = row[53]
                if row[56] not in meaning['nationality'].keys() and row[56] != '':
                    meaning['nationality'][row[56]] = row[57]
                    
                data[key]['target'] = {'type': [row[35], row[43], row[51]] , 'subtype': [row[37], row[45], row[53]],
                                        'corporation': [row[38], row[46], row[54]], 'target': [row[39], row[47], row[55]],
                                        'nationality': [row[41], row[49], row[57]]} #nationality from meaning['country'][...]
                                       

                                

                data[key]['group_name'] = [row[58], row[60], row[62]]
                data[key]['group_subname'] = [row[59], row[61], row[63]]

                data[key]['motive'] = row[64]
             

                            

                data[key]['group_confirmed'] = [row[65], row[66], row[67]]
                if (row[68]=="-99" or row[68]==""):
                    row[68]="Unknown"
                data[key]['perps'] = row[68]    #-99 is unknown; blank is unknown
                if (row[69]=="-99" or row[69]==""):
                    row[69]="Unknown"
                data[key]['perpsCaptured'] = row[69]

                
                if row[71] not in meaning['claim_mode'] and row[71] != '':
                    meaning['claim_mode'][row[71]] = row[72]
                if row[74] not in meaning['claim_mode'] and row[74] != '':
                    meaning['claim_mode'][row[74]] = row[75]
                if row[77] not in meaning['claim_mode'] and row[77] != '':
                    meaning['claim_mode'][row[77]] = row[78]
                data[key]['claimed'] = [[row[70], row[72]], [row[73], row[75]], [row[76], row[78]]] #0/1, mode(1-10)
                
                data[key]['weapon']={'type': [row[81], row[85], row[89], row[93]],
                                     'subtype': [row[83], row[87], row[91], row[95]],
                                     'details': row[96]}
                if row[80] not in meaning['weapon_type'].keys() and row[80] != '':
                    meaning['weapon_type'][row[80]] = row[81]
                if row[84] not in meaning['weapon_type'].keys() and row[84] != '':
                    meaning['weapon_type'][row[84]] = row[85]
                if row[88] not in meaning['weapon_type'].keys() and row[88] != '':
                    meaning['weapon_type'][row[88]] = row[89]
                if row[92] not in meaning['weapon_type'].keys() and row[92] != '':
                    meaning['weapon_type'][row[92]] = row[93]
                if row[82] not in meaning['weapon_subtype'].keys() and row[82] != '':
                    meaning['weapon_subtype'][row[82]] = row[83]
                if row[86] not in meaning['weapon_subtype'].keys() and row[86] != '':
                    meaning['weapon_subtype'][row[86]] = row[87]
                if row[90] not in meaning['weapon_subtype'].keys() and row[90] != '':
                    meaning['weapon_subtype'][row[90]] = row[91]
                if row[94] not in meaning['weapon_subtype'].keys() and row[94] != '':
                    meaning['weapon_subtype'][row[94]] = row[95]


                                    

                data[key]['kills'] = [row[97], row[98], row[99]]

                
                        
                    #[kills, killsUS, killsProp]
                data[key]['wounds'] = [row[100], row[101], row[102]]

                

                        

                data[key]['property'] = [row[103], row[104], row[106], row[107]] #row[103] is 1/0/-9 = yes/now/unknown
                    # yes/no/unk , null or 1-4, value, comment

                

                        

                data[key]['hostages'] = [row[108], row[109], row[110], row[111], row[112], row[122], row[123]]

                
                
                    #yes/no null , nr host, nr host US, hours, days , outcome key, released
                if row[121] not in meaning['hostages_outcome'].keys() and row[121] != '':
                    meaning['hostages_outcome'][row[121]] = row[122]

                data[key]['ransom'] = [row[115], row[116], row[117], row[118], row[119], row[120]]
                    #yes/no null, value, value US, paid, paid US, note

                        

                data[key]['notes'] = row[124]
                data[key]['sources'] = [row[125], row[126], row[127]]
                data[key]['related'] = row[133].split(',')


                #########################################################################
                #Second Part
                #########################################################################
                ok=0

                
                if data[key]["group_name"][0] not in org.keys() and data[key]["group_name"][0] != '':
                    org[data[key]["group_name"][0]] = {'area': [], 'parteners': [], 'subname': [], 'alternative': {}, 'atack_type': {}, 'year': {}, 'target_subtype': {}, "motive": {}, "weapon_subtype": {}, 'nkill': 0, 'nwound': 0, 'prop_value': 0, 'hostages': 0, 'ransom_given': 0}
                if data[key]["group_name"][0] in org.keys() and data[key]["group_subname"][0] != '' and data[key]['group_subname'][0] not in  org[data[key]["group_name"][0]]['subname'] and data[key]["group_name"][0] in org.keys():
                    org[data[key]["group_name"][0]]['subname'] += [data[key]["group_subname"][0]]
                if data[key]["group_name"][1] not in org.keys() and data[key]["group_name"][1] != '':
                    org[data[key]["group_name"][1]] = {'area': [], 'parteners': [], 'subname': [], 'alternative': {}, 'atack_type': {}, 'year': {}, 'target_subtype': {}, "motive": {}, "weapon_subtype": {}, 'nkill': 0, 'nwound': 0, 'prop_value': 0, 'hostages': 0, 'ransom_given': 0}
                if data[key]["group_name"][1] in org.keys() and data[key]["group_subname"][1] != '' and data[key]['group_subname'][1] not in  org[data[key]["group_name"][1]]['subname'] and data[key]["group_name"][1] in org.keys():
                    org[data[key]["group_name"][1]]['subname'] += [data[key]["group_subname"][1]]
                if data[key]["group_name"][2] not in org.keys() and data[key]["group_name"][2] != '':
                    org[data[key]["group_name"][2]] = {'area': [], 'parteners': [], 'subname': [], 'alternative': {}, 'atack_type': {}, 'year': {}, 'target_subtype': {}, "motive": {}, "weapon_subtype": {}, 'nkill': 0, 'nwound': 0, 'prop_value': 0, 'hostages': 0, 'ransom_given': 0}
                if data[key]["group_name"][2] in org.keys() and data[key]["group_subname"][2] != '' and data[key]['group_subname'][2] not in  org[data[key]["group_name"][2]]['subname'] and data[key]["group_name"][2] in org.keys():
                    org[data[key]["group_name"][2]]['subname'] += [data[key]["group_subname"][2]]

                for x in data[key]["group_name"]:
                    if x!='':
                        ok+=1
                if ok==2:
                    if data[key]["group_name"][1] not in org[data[key]["group_name"][0]]['parteners']:
                        org[data[key]["group_name"][0]]['parteners'] += [data[key]["group_name"][1]]
                    if data[key]["group_name"][0] not in org[data[key]["group_name"][1]]['parteners']:
                        org[data[key]["group_name"][1]]['parteners'] += [data[key]["group_name"][0]]
                elif ok==3:
                    if data[key]["group_name"][1] not in org[data[key]["group_name"][0]]['parteners']:
                        org[data[key]["group_name"][0]]['parteners'] += [data[key]["group_name"][1]]
                    if data[key]["group_name"][2] not in org[data[key]["group_name"][0]]['parteners']:
                        org[data[key]["group_name"][0]]['parteners'] += [data[key]["group_name"][2]]
                    if data[key]["group_name"][0] not in org[data[key]["group_name"][1]]['parteners']:
                        org[data[key]["group_name"][1]]['parteners'] += [data[key]["group_name"][0]]
                    if data[key]["group_name"][2] not in org[data[key]["group_name"][1]]['parteners']:
                        org[data[key]["group_name"][1]]['parteners'] += [data[key]["group_name"][2]]
                    if data[key]["group_name"][0] not in org[data[key]["group_name"][2]]['parteners']:
                        org[data[key]["group_name"][2]]['parteners'] += [data[key]["group_name"][0]]
                    if data[key]["group_name"][1] not in org[data[key]["group_name"][2]]['parteners']:
                        org[data[key]["group_name"][2]]['parteners'] += [data[key]["group_name"][1]]

                ### move to 2
                if (row[23]!=''):
                    for x in range (0,ok):
                        if row[24] in org[data[key]["group_name"][x]]['alternative'].keys():
                            org[data[key]["group_name"][x]]['alternative'][row[24]]+=1
                        else:
                            org[data[key]["group_name"][x]]['alternative'][row[24]]=1

                for x in range (0,ok):
                    if row[1] in org[data[key]["group_name"][x]]['year'].keys():
                        org[data[key]["group_name"][x]]['year'][row[1]]+=1
                    else:
                        org[data[key]["group_name"][x]]['year'][row[1]]=1
                            

                for x in range (0,ok):
                    if (row[9] not in org[data[key]["group_name"][x]]['area']):
                        org[data[key]["group_name"][x]]['area']+=[row[9]]

                
                ### move to 2
                for at in data[key]['atacktype']:
                    for x in range (0, ok):
                        if at in org[data[key]["group_name"][x]]['atack_type'].keys() and at!='':
                            org[data[key]["group_name"][x]]['atack_type'][at]+=1
                        elif at!='':
                            org[data[key]["group_name"][x]]['atack_type'][at]=1
                

                ### move to 2
                for at in data[key]['target']['subtype']:
                    for x in range (0, ok):
                        if at in org[data[key]["group_name"][x]]['target_subtype'].keys() and at!='':
                            org[data[key]["group_name"][x]]['target_subtype'][at]+=1
                        elif at!='':
                            org[data[key]["group_name"][x]]['target_subtype'][at]=1


                ### move to 2
                if data[key]['motive'] != '' and data[key]['motive']!='Unknown':
                    for x in range (0, ok):
                        if data[key]['motive'] in org[data[key]["group_name"][x]]['motive']:
                            org[data[key]["group_name"][x]]['motive'][data[key]['motive']]+=1
                        else:
                            org[data[key]["group_name"][x]]['motive'][data[key]['motive']]=1

                ###move to 2
                for at in data[key]['weapon']['subtype']:
                    for x in range (0, ok):
                        if at in org[data[key]["group_name"][x]]['weapon_subtype'] and at!='':
                            org[data[key]["group_name"][x]]['weapon_subtype'][at]+=1
                        elif at!= '':
                            org[data[key]["group_name"][x]]['weapon_subtype'][at]=1

                ### move to 2
                for x in range (0,ok):
                    if (data[key]['kills'][0]!= ''):
                        org[data[key]["group_name"][x]]['nkill']+= int(float(data[key]['kills'][0]))


                ### move to 2
                for x in range (0,ok):
                    if (data[key]['wounds'][0]!= ''):
                        org[data[key]["group_name"][x]]['nwound']+= int(float(data[key]['wounds'][0]))


                ### move to 2
                for x in range (0,ok):
                    if (data[key]['property'][2]!= ''):
                        org[data[key]["group_name"][x]]['prop_value']+= int(float(data[key]['property'][2]))


                ### move to 2
                for x in range (0,ok):
                    if (data[key]['hostages'][1]!= ''):
                        org[data[key]["group_name"][x]]['hostages']+= int(float(data[key]['hostages'][1]))

                ### move to 2
                for x in range (0,ok):
                    if (data[key]['ransom'][3]!= ''):
                        org[data[key]["group_name"][x]]['ransom_given']+= int(float(data[key]['ransom'][3]))

                            
                
            i = False
                

        f.close()

    


def similarities(organisation, numbertoreturn=5):
    sim=[]
    for o in org.keys():
        ss=0.0
        maxsim=100.0
        if o!=organisation and o!="NewEvent":
            if org[o]['alternative'] == org[organisation]['alternative']:
                ss+=5
                   
            if len(org[o]['atack_type'].keys())>0:
                nbTot=len(org[o]['atack_type'].keys())
                nb=0
                for t in org[organisation]['atack_type'].keys():
                    if t in org[o]['atack_type'].keys():
                        nb+=1
                ss+=(float(nb)/nbTot)*5
            elif len(org[o]['atack_type'].keys())==0 and len(org[o]['atack_type'].keys())==len(org[organisation]['atack_type'].keys()):
                maxsim-=5
            

            if len(org[o]['target_subtype'].keys())>0:
                nbTot=len(org[o]['target_subtype'].keys())
                nb=0
                for t in org[organisation]['target_subtype'].keys():
                    if t in org[o]['target_subtype'].keys():
                        nb+=1
                ss+=(float(nb)/nbTot)*10
            elif len(org[o]['target_subtype'].keys())==0 and len(org[o]['target_subtype'].keys())==len(org[organisation]['target_subtype'].keys()):
                maxsim-=10

            if len(org[o]['motive'].keys())>0:
                nbTot=len(org[o]['motive'].keys())
                nb=0
                for t in org[organisation]['motive'].keys():
                    if t in org[o]['motive'].keys():
                        nb+=1
                ss+=(float(nb)/nbTot)*20
                if nb>0:
                    ss+=40
            elif len(org[o]['motive'].keys())==0 and len(org[o]['motive'].keys())==len(org[organisation]['motive'].keys()):
                maxsim-=60
                
            if len(org[organisation]['weapon_subtype'].keys())>0:
                nbTot=len(org[organisation]['weapon_subtype'].keys())
                nb=0
                for t in org[organisation]['weapon_subtype'].keys():
                    if t in org[o]['weapon_subtype'].keys():
                        nb+=1
                ss+=(float(nb)/nbTot)*5
            elif len(org[o]['weapon_subtype'].keys())==0 and len(org[o]['weapon_subtype'].keys())==len(org[organisation]['weapon_subtype'].keys()):
                maxsim-=5


            for tp in ["nkill", "nwound", "prop_value", "hostages", "ransom_given"]:
                if org[organisation][tp]<org[o][tp] and org[o][tp]!=0:
                    ss+=(float(org[organisation][tp])/org[o][tp])*2
                elif org[organisation][tp]>0 and org[organisation][tp]:
                    ss+=(float(org[o][tp])/org[organisation][tp])*2
                if (org[organisation][tp]>0 and org[o][tp]>0) or (org[organisation][tp]==org[o][tp]):
                    ss+=1

            ############################################### For UNKNOWN
            if organisation == "NewEvent":
                maxsim+=35
                if org[organisation]['area'][0] in org[o]['area']:
                    ss+=25
                elif len(org[o]['area'])==0 or len(org[organisation]['area'])==0:
                    maxsim-=25
                elif int(org[organisation]['area'][0]) in range (1,4):
                    ok=0
                    for a in org[o]['area']:
                        if int(a) in range (1, 4):
                            ok=1
                    if ok==1:
                        ss+=8
                elif int(org[organisation]['area'][0]) in range (4,8):
                    ok=0
                    for a in org[o]['area']:
                        if int(a) in range (4, 8):
                            ok=1
                    if ok==1:
                        ss+=8
                elif int(org[organisation]['area'][0]) in [8, 9, 12]:
                    ok=0
                    for a in org[o]['area']:
                        if int(a) in [8, 9, 12]:
                            ok=1
                    if ok==1:
                        ss+=8
                elif int(org[organisation]['area'][0]) in range (10,12):
                    ok=0
                    for a in org[o]['area']:
                        if int(a) in range (10, 12):
                            ok=1
                    if ok==1:
                        ss+=8

                dYear=6
                YY=int(org[organisation]['year'])
                for y in org[o]['year'].keys():
                    if YY>int(y):
                        if dYear> YY-int(y):
                            dYear = YY-int(y)
                    elif dYear> int(y)-YY:
                        dYear = int(y)-YY
                if dYear<=5:
                    ss+=(5-dYear)*2
                    
                    
                

            ##############################################

            sim+=[((ss/maxsim)*100,o)] #[["name",%],[],[]]
    sim.sort()
    return sim[len(sim)-numbertoreturn:]
        


def callEvent(key):
    org['NewEvent']= {'area': [data[key]['location']['region']], 'parteners': [], 'subname': [], 'alternative': {}, 'atack_type': {}, 'target_subtype': {}, "motive": {}, "weapon_subtype": {}, 'nkill': 0, 'nwound': 0, 'prop_value': 0, 'hostages': 0, 'ransom_given': 0}

    if data[key]['alternative'] != '':
        org['NewEvent']['alternative'][data[key]['alternative']] = 1
        
    for at in data[key]['atacktype']:
        if at in org["NewEvent"]['atack_type'].keys() and at!='':
            org['NewEvent']['atack_type'][at]+=1
        elif at!='':
            org["NewEvent"]['atack_type'][at]=1
            
    for at in data[key]['target']['subtype']:
        if at in org["NewEvent"]['target_subtype'].keys() and at!='':
            org["NewEvent"]['target_subtype'][at]+=1
        elif at!='':
            org["NewEvent"]['target_subtype'][at]=1

    if data[key]['motive'] != '' and data[key]['motive']!='Unknown':
        if data[key]['motive'] in org["NewEvent"]['motive']:
            org["NewEvent"]['motive'][data[key]['motive']]+=1
        else:
            org["NewEvent"]['motive'][data[key]['motive']]=1

    ###move to 2
    for at in data[key]['weapon']['subtype']:  
        if at in org["NewEvent"]['weapon_subtype'] and at!='':
            org["NewEvent"]['weapon_subtype'][at]+=1
        elif at!= '':
            org["NewEvent"]['weapon_subtype'][at]=1

    ### move to 2
    if (data[key]['kills'][0]!= ''):
        org["NewEvent"]['nkill']+= int(float(data[key]['kills'][0]))

    org["NewEvent"]['year']= data[key]['date']['year']


    ### move to 2
    if (data[key]['wounds'][0]!= ''):
        org["NewEvent"]['nwound']+= int(float(data[key]['wounds'][0]))


    ### move to 2
    if (data[key]['property'][2]!= ''):
        org["NewEvent"]['prop_value']+= int(float(data[key]['property'][2]))


    ### move to 2
    if (data[key]['hostages'][1]!= ''):
        org["NewEvent"]['hostages']+= int(float(data[key]['hostages'][1]))

    ### move to 2

    if (data[key]['ransom'][3]!= ''):
        org["NewEvent"]['ransom_given']+= int(float(data[key]['ransom'][3]))

    return similarities("NewEvent")



reader()
org.pop("Unknown", None)

#call -> callEvent(idx) for Event + org.pop("NewEvent", None)

#OR

#call -> similarities(organisation_name) which returns [[%, toOrganisation]]





#print "Done Reading"

#for idx in data.keys():
#    if data[idx]['group_name'][0] in ["", "Unknown"]:
#        if "NewEvent" in org.keys():
#            org.pop("NewEvent", None)
#        z = callEvent(idx)
#        if z[len(z)-1][0] > 90.0:
#            print idx+" has a "+str(z[len(z)-1][0])[:4]+"% similarity to "+z[len(z)-1][1]
        
#if __name__ == "__main__":
#    while True:
#        a = raw_input ("TRY ME: ")
#        if a=="Unknown":
#            a = raw_input ("Id: ")
#            if "NewEvent" in org.keys():
#                org.pop("NewEvent", None)
#            z = callEvent(a)
#            for i in range (0, 5):
#                print "NewEvent has a "+str(z[len(z)-1-i][0])[:4]+"% similarity to "+z[len(z)-1-i][1]
#        elif a in org.keys():
#            z = similarities(a)
#            for i in range (0, 5):
#                print a+" has a "+str(z[len(z)-1-i][0])[:4]+"% similarity to "+z[len(z)-1-i][1]
#        elif a=="STOP":
#            break
#        else:
#            print "Try Again"



        

