#create a JSON file that includes only the objects that include all of the provenance information as mentioned below, and to count how many objects actually have the information 

import glob
import json


#need the following: accessionYear, culture, artistDisplayName, artistDisplayBio, objectBeginDate, objectEndDate

save_data = []

has_city = 0
has_artistDisplayName = 0
has_accessionYear = 0
has_culture = 0
has_artistDisplayBio = 0
has_objectBeginDate = 0
has_objectEndDate = 0

for filename in glob.glob('Object_IDs/*.json'):
    #print(filename)
    with open(filename, 'r') as jsonfile:
        data = json.load(jsonfile)
        if (data['city']) != '' and (data['country']) != '' and (data['state']) != '' and (data['artistDisplayName']) != '' and (data['culture']) != '' and (data['accessionYear']) != '' and (data['artistDisplayBio']) != '' and (data['objectBeginDate']) != '' and (data['objectEndDate']) != '':
            save_data.append(data)
            has_city+=1
            has_artistDisplayName+=1
            has_accessionYear+=1
            has_culture+=1
            has_artistDisplayBio+=1
            has_objectBeginDate+=1
            has_objectEndDate+=1
        print(data['city'])
        print(data['artistDisplayName'])
        print(data['accessionYear'])
        print(data['culture'])
        print(data['artistDisplayBio'])
        print(data['objectBeginDate'])
        print(data['objectEndDate'])


with open ('p', 'w') as out:
    json.dump(save_data,out,indent=2)

print(has_city)
print(has_artistDisplayName)
print(has_culture)
print(has_accessionYear)
print(has_artistDisplayBio)
print(has_objectBeginDate)
print(has_objectEndDate)