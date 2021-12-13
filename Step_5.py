# 1. Write a script download every object (from the web scrape) id from the MET API and save it as its own json file (obj1235.json)
# 	1a. Write out every prov statment to a text file so you can sort them and decided what data to extract
# 	1b. Write some regular expressions to pull out specific data peices from the prov statment
# 	1c. Look at other fields in the each json file (obj1235.json) for other prov related field that might be useful
# 	1d. Make some vizs around the data you found (75% have a date, 20% have a person's name)
# 2. Write a script reads each of the json file (obj1235.json) and pulls out the relevent prov data peices and turns it into linked art json ld json files (like below)


# {
#   "@context": "https://linked.art/ns/v1/linked-art.json",
#   "id": "https://linked.art/example/provenance/5",
#   "type": "Activity",
#   "_label": "Gift of two Paintings to Museum",
#   "classified_as": [
#     {
#       "id": "http://vocab.getty.edu/aat/300055863",
#       "type": "Type",
#       "_label": "Provenance Activity"
#     },
#     {
#       "id": "http://vocab.getty.edu/aat/300417637",
#       "type": "Type"
#     }
#   ],
#   "part": [
#     {
#       "type": "Acquisition",
#       "_label": "Acquisition of Painting 1"
#     },
#     {
#       "type": "Acquisition",
#       "_label": "Acquisition of Painting 2"
#     }
#   ]
# }
# "timespan": {
#     "type": "TimeSpan",
#     "begin_of_the_begin": "2002-04-19T00:00:00Z",
#     "end_of_the_end": "2002-04-26T00:00:00Z"
#   },

import json    


with open('All_Obs_With_Prov.json', 'r') as jsonfile:
    data = json.load(jsonfile)


all_prov_statements = []


# for loop here that loop through every json API obj file and opens it and lods it with json
for all_prov_statement in data: 
    if (data['creditline']) != '' and (data['prov']) != '':
        print(data['creditline'])


#	in this loop pull out the fields that to use to get readdy to make the prov_activty below

counter= 1
prov_activty = {}



# this would be for one file




all_prov_statements.append(prov_activty)


json.dump(all_prov_statements,open('linked_art_prov_examples.json','w'),indent=2)








