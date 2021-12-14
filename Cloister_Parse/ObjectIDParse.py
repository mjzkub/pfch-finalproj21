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