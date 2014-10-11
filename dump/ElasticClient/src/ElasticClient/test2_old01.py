import csv
import string

data = {}
meaning = {}
meaning['country'] = {}
meaning['region'] = {}
# meaning criterion
meaning['alternative'] = {"1": "Insurgency/Guerilla Action", "2": "Other Crime Type", "3": "Intra/Inter-group Conflict", "4": "Lack of Intentionality"}
meaning['atack_type'] = {'1': 'Assassination', '2': 'Armed Assault', '3': 'Bombing/Explosion', '4': 'Hijacking', '5': 'Hostage Taking (Barricade Incident)',
                         '6': 'Hostage Taking (Kidnapping)', '7':'Facility/Infrastructure Attack', '8': 'Unarmed Assault', '9': 'Unknown'}
meaning['target_type'] = {}
meaning['target_subtype'] = {}
meaning['nationality'] = {}
meaning['claim_mode'] = {}
meaning['weapon_type'] = {}
meaning['weapon_subtype'] = {}
meaning['property'] = { '1': 'Catastrophic (likely > $1 billion)', '2': 'Major (likely > $1 million but < $1 billion)',
                        '3': 'Minor (likely < $1 million)', '4': 'Unknown'}
meaning['hostages_outcome'] = {}


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

                data[key]['atacktype'] = [row[28], row[30], row[32]]

                data[key]['target'] = [{'type': [row[34], row[42], row[50]] , 'subtype': [row[36], row[44], row[52]],
                                        'corporation': [row[38], row[46], row[54]], 'target': [row[39], row[47], row[55]],
                                        'nationality': [row[40], row[48], row[56]]}, #nationality from meaning['country'][...]
                                       ]
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

                data[key]['group_name'] = [row[58], row[60], row[62]]
                data[key]['group_subname'] = [row[59], row[61], row[63]]

                data[key]['motive'] = row[64]

                data[key]['group_confirmed'] = [row[65], row[66], row[67]]

                data[key]['perps'] = row[68]    #-99 is unknown; blank is unknown
                data[key]['perpsCaptured'] = row[69]

                data[key]['claimed'] = [[row[70], row[71]], [row[73], row[74]], [row[76], row[77]]] #0/1, mode(1-10)
                if row[71] not in meaning['claim_mode'] and row[71] != '':
                    meaning['claim_mode'][row[71]] = row[72]
                if row[74] not in meaning['claim_mode'] and row[74] != '':
                    meaning['claim_mode'][row[74]] = row[75]
                if row[77] not in meaning['claim_mode'] and row[77] != '':
                    meaning['claim_mode'][row[77]] = row[78]

                data[key]['weapon']={'type': [row[80], row[84], row[88], row[92]],
                                     'subtype': [row[82], row[86], row[90], row[94]],
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

                data[key]['hostages'] = [row[108], row[109], row[110], row[111], row[112], row[121], row[123]]
                    #yes/no null , nr host, nr host US, hours, days , outcome key, released
                if row[121] not in meaning['hostages_outcome'].keys() and row[121] != '':
                    meaning['hostages_outcome'][row[121]] = row[122]

                data[key]['ransom'] = [row[115], row[116], row[117], row[118], row[119], row[120]]
                    #yes/no null, value, value US, paid, paid US, note

                data[key]['notes'] = row[124]
                data[key]['sources'] = [row[125], row[126], row[127]]
                data[key]['related'] = row[133].split(',')
                
                
            i = False
                

        f.close()



reader()

