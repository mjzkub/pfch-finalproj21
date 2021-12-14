# access the met's provenance collection website, and filter out for only Nazi-Era Provenance objects withtin the clositers
# use devloper tool to pull specific URLs
# go to URLs and copy and paste JSON data
# save one new json file per page (this is where the below json files came from)
#split the url and webscrape in order to get the inidividual object IDs in one file


import json
ObjectId = []

files = ["cloister1.json" , "cloister2.json" , "cloister3.json" , "cloister4.json" , "cloister5.json" , "cloister6.json" , "cloister7.json" , "cloister8.json" , "cloister9.json" , "cloister10.json" , "cloister11.json" , "cloister12.json" , "cloister13.json" , "cloister14.json" , "cloister15.json" ]

for file in files:
    with open (file) as f:
        data = json.load(f)
        
        for record in data["results"]:
            print(record)

            url = record["url"]

            number = url.split('/search/')[1]
            number = number.split('?')[0]
            ObjectId.append(number)

with open ('ObjectIDs.json' , 'w') as f:
    json.dump(ObjectId , f)