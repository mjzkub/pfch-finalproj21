import json
import re

all_linked_art = []
counter = 0

with open('All_Obs_With_Prov.json', 'r') as jsonfile:
    data = json.load(jsonfile)


    for obj in data:


        # here we have each obj
        # we can pull out the prov into own var

        prov = obj['prov']
        accession_type = obj['creditLine']
        


        # here is where you need to take a look at all the possiblities with what you could do with various prov statments
        # if creditline contains "gift of" then the _label should be different .. need to do regex to pull that out 

        # but assume each one contains multiple stamtenents seperated by ";" you can split them into a list

        prov_statements = prov.split(';')
        credit_statments =  accession_type.split(';')

        # and now loop through each split statement

        # for prov in prov_statements:
        

        #     # print(prov)


        #     # you can do a lot of stuff here using regular expressions
        #     # you need to look at the statements to see what else can be done
             
        #     # see if there is a "sold xxxx" date pattern
        #     sold_year = re.search(r"sold ([0-9]{4})",prov)
 

        #     # if that found something
        #     if sold_year != None:
                
        #         year = sold_year.group(1)

        #         counter = counter + 1

        #         ld_statment = {
        #           "@context": "https://linked.art/ns/v1/linked-art.json",
        #           "id": f"https://metmuseum.org/prov/provenance/{counter}",
        #           "type": "Activity",
        #           "_label": accession_type , 
        #           "classified_as": [
        #             {
        #               "id": "http://vocab.getty.edu/aat/300055863",
        #               "type": "Type",
        #               "_label": "Provenance Activity"
        #             }
        #           ],
        #           "timespan": {
        #             "type": "TimeSpan",
        #             "begin_of_the_begin": f"{year}-01-01T00:00:00Z",                    
        #           },
        #           "carried_out_by": [
        #             {
        #               "type": "Group",
        #               "_label": prov
        #             }
        #           ],
        #           "part" : [
        #             {
        #             "type": "Acquisition" ,
        #             "_label": "Acquisition of Object"
        #             }
        #           ]
        #         }

        #         print(ld_statment)

        #         all_linked_art.append(ld_statment)


        #         continue


        # we dont need  loop here, since it is just one string
        # for accession_type in credit_statments:

          # does it have the key words
        gift_prov = re.search(r"Gift\sof" , accession_type)

        if gift_prov != None:



            print("Found gift accession_type",accession_type)

            # try to pull out the year
            gift_year = re.search(r"([0-9]{4})",accession_type)


            if gift_year != None:

              year = gift_year.group(1)

              print('Found year!', year)
              ld_statment = {
                "@context": "https://linked.art/ns/v1/linked-art.json",
                "id": f"https://metmuseum.org/prov/provenance/{counter}",
                "type": "Activity",
                "_label": accession_type , 
                "classified_as": [
                  {
                    "id": "http://vocab.getty.edu/aat/300055863",
                    "type": "Type",
                    "_label": "Provenance Activity"
                  }
                ],
                "timespan": {
                  "type": "TimeSpan",
                  "begin_of_the_begin": f"{year}-01-01T00:00:00Z",                    
                },
                "carried_out_by": [
                  {
                    "type": "Group",
                    "_label": prov
                  }
                ],
                "part" : [
                  {
                  "type": "Acquisition" ,
                  "_label": "Acquisition of Object" 
                  }
                ]
              }


              print(ld_statment)

              all_linked_art.append(ld_statment)
            else:

              print("Found 'gift of' but no year! cannot make statement", accession_type)
            


json.dump(all_linked_art,open('linked_art_prov_examples.json','w'),indent=2)






# all_prov_statements = []


# # for loop here that loop through every json API obj file and opens it and lods it with json
# for all_prov_statement in data: 
#     if (data['creditline']) != '' and (data['prov']) != '':



# #	in this loop pull out the fields that to use to get readdy to make the prov_activty below

# counter= 1
# prov_activty = {}



# # this would be for one file
# prov_activty['@context'] = data('creditline')
# prov_activty['id'] = data('objectURL')
# #prov_activty['type'] =
# prov_activty["_label"] = data('prov')

# #prov_activty['timespan'] = []

# #prov_activty['timespan']['type']= []
# #prov_activty['timespan']['begin_of_the_begin'] = []
# prov_activty['timespan']['end_of_the_end'] = data('accessionYear')



# all_prov_statements.append(prov_activty)


# json.dump(all_prov_statements,open('linked_art_prov_examples.json','w'),indent=2)












