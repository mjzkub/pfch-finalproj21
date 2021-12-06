import json
import requests

# load the contents of json file into a var
objectIds = json.load(open('ObjectIDs.json'))

# loop through this var, since the json file was one big list

for objectId in objectIds:

    # build a new url
    url = f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{objectId}'
    print("Doing:",url)

    r = requests.get(url)

    # turn it into python data
    objectData = json.loads(r.text)

    # save the results out to its own file
    json.dump(objectData, open(f'{objectId}.json','w'),indent=2)