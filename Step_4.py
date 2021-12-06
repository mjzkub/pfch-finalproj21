#this step is necesscary to create Tableau visualizations, the conversion of JSON to CSV. The file "All_Obs" is a result of a variation of code from Step 3
#this variation is noted in the second line of step 3

import json
import csv
 
with open('All_Obs.json') as json_file:
    jsondata = json.load(json_file)
 
data_file = open('All_Obs.csv', 'w', newline='')
csv_writer = csv.writer(data_file)
 
count = 0
for data in jsondata:
    if count == 0:
        header = data.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(data.values())
 
data_file.close()

