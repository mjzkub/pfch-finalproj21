import json
import requests
import glob

from bs4 import BeautifulSoup

#use curl converter 

all_data = []

# loop through all the ids we have
for obj_filename in glob.glob('Object_IDs/*.json'):
	# load the data
	data = json.load(open(obj_filename))

	objId = data['objectID']

	# request that webpage from the met catalog with prov info
	url = f"https://www.metmuseum.org/art/collection/search/{objId}"

	headers = {

    'authority': 'www.metmuseum.org',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'visid_incap_1661977=3oOWPV/PTjuVYv7FX3zsGkFmgGEAAAAAQUIPAAAAAADSRIIH7ZkC8YgH9ynWL1Y6; visid_incap_1662004=FYHa3DmeRli8JxFw5s/r4UFmgGEAAAAAQUIPAAAAAACvsDccP6LXvzvQCfE1LGb3; optimizelyEndUserId=oeu1635804738949r0.41432896696397825; _gcl_au=1.1.82181991.1635804739; _ga=GA1.2.1132316961.1635804739; _fbp=fb.1.1635804739607.158905316; __qca=P0-1314414302-1635804739616; __atuvc=1%7C45; __utma=85941765.1132316961.1635804739.1636422390.1636422390.1; __utmz=85941765.1636422390.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); visid_incap_2349797=I5ivh1D9R0+ndNZMXUZSsN/ZiWEAAAAAQUIPAAAAAAC3DpXk5ziHy1F5sZ750Il7; visid_incap_1661922=7jILg4kESByrBOk+mXYRlj1mgGEAAAAAQ0IPAAAAAACA8lCgAdF683KvWxA34Za9HwsEg9/u9JbR; ki_r=; ki_s=221516%3A0.0.0.0.0; ObjectPageSet=0.102090366697912; incap_ses_7223_1661922=80xtBI3mOGsj82KbjEA9ZCZ/smEAAAAA+7OkMbv3xxx5WLD4S1+rfw==; incap_ses_7223_1662004=Uh+6Ob3FYG9wH2ObjEA9ZCZ/smEAAAAAp5lHxHqxjoPXhNh1pCgGpQ==; _gid=GA1.2.1929735734.1639087912; _parsely_session={%22sid%22:9%2C%22surl%22:%22https://www.metmuseum.org/art/collection/search/479686%22%2C%22sref%22:%22%22%2C%22sts%22:1639087911754%2C%22slts%22:1638577974557}; _parsely_visitor={%22id%22:%22pid=3d32a2ed494deec7491e254038081652%22%2C%22session_count%22:9%2C%22last_session_ts%22:1639087911754}; _dc_gtm_UA-72292701-1=1; ki_t=1635804739753%3B1639087912190%3B1639087935576%3B6%3B225',
}
	r = requests.get(url , headers=headers)
	# parse it 
	soup = BeautifulSoup(r.text, "html.parser")

	# look from the <h2>Provenance</h2>

	element_prov_h2 = soup.find('h2',text="Provenance")

	# get the <h2> parent's parent or grand parent because it holds the h2 and prov text
	element_prov_container = element_prov_h2.parent.parent
	# now look into that for the prov div
	element_prov = element_prov_container.find('div',{'class':'accordion__content'})
	# and get the text of it
	prov_text = element_prov.text
	# clean it up a little
	prov_text = prov_text.strip()

	# now add it back into the json data and ssave it out again
	data['prov'] = prov_text

	all_data.append(data)

with open('All_Obs_With_Prov.json','w') as outfile:
	json.dump(all_data,outfile,indent=2)