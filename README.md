# pfch-finalproj21
Project overview: 

The purpose of my project is to examine the metadata available for Nazi-era Provenance paintings within The Metropolitan Museum of Art’s Provenance Research Collection and determine if there is sufficient provenance information to serialize these objects Linked Art's Provenance modeling. The parameters for this model type can be found here; in short, the model deals mostly with provenance “activities” or “events.” These elements will relay information such as transfers of custody, acquisition activity, and object rediscovery.

A note about Nazi-era Provenance: 

During WWII, the Nazi party looted over one million artworks from various sources. Though the Nazi Regime stole artwork for various reasons, each justification relies on the idea of "ethnic cleansing." For example, the Nazis looted art created by those persecuted in the Holocaust, including Jewish people, disabled folks, people of color, those in the LGBTQIA+ community, and Romas. Such art pieces were detrimental to the Nazi sentiment because they celebrated the talents of those diaspora mentioned and/or depicted modernist art movements such as expressionism and abstract. The Nazis considered modernist art an insult to the "German feeling" as their art style of choice was classical art that depicted "Hellenistic" beauty; only in this context, Hellenistic functions as a synonym for "Aryan. 
 
While some of these pieces met the unfortunate fate of immediate destruction, some ended up in art exhibits created to mock the aforementioned groups. Entartete Kunst (The Degenerate Art Exhibition) produced by Adolf Ziegler and the Nazi Party is another example of how taking control of cultural institutions is a forceful, deeply nefarious facet of a fascist power grab. This exhibition displayed more than 700 works of modernist art for the sole purpose of vilification (Clark, 1997). The pieces ranged the spectrum of modernist art movements, including expressionist and abstract art. The exhibit organization was deliberately sloppy: pictures were hung erratically, paintings were unframed, and a price accompanied some pieces to show their low-monetary worth. Attendees of the presentation were encouraged to laugh at the display and make rude remarks. "Degeneracy" was a crucial idea in Nazi theory and functioned as a method of portraying the persecuted groups' "genetic deformities".
 
Although the disrespect and humiliation levied against these artworks were despicable, at least the pieces were preserved to some degree. Those artworks spared a fate of destruction, including those used in exhibits such as Entartete Kunst, constitute a body of work with "Nazi-era Provenance." 
 
With all of this in mind, it is clear that such provenance is highly dependent on event documentation in an artwork's life, including those elements specified by the Linked Art's Provenance model. 


Dataset: 

In order to narrow the scope of my project, my dataset only includes paintings held at the Met’s Cloisters with Nazi-era Provenance. There are 1,155 objects within this narrowed scope. The decision to only examine paintings greatly decreased the number of objects, as there are a multitude of different art mediums utilized in this collection. 

Method: 

Below I will break down my methods in steps; the python code utilized in each of these steps and the resulting JSON files can be found on this repository:

Step 1: Use webscraping to download Nazi-era Provenance objects from the provenance research project list. This step required a URL split stage, which was achieved by going through all 15 pages of the filtered collection, opening the developer tool, and using that specific URL to download a list of Object IDs.  
Step 2: Use a secret API to download each Object as a JSON file with their respective metadata. 
Step 3: Use regular expressions and glob create a JSON file with a list of object metadata which include data that can be used for provenance. At this time, I noticed there is virtually no “event” specific provenance data, so I pulled out information that could be used for provenance through inductive reasoning: 
	1. Artist Name
	2. Culture (culture depicted in art or culture of the artist)
	3. Accession Year
	4. Object Begin/End Date
	5. Artist Bio
	6. City (typically coincides with culture)
	7. Country (typically coincides with culture)
	8. State (typically coincides with culture)

Step 4: Slightly edit code in Step 3 to create single a JSON file with all of the metadata for each object, then create new code to convert the JSON file to CSV in order to create Tableau visualizations (available on project site)  
Step 5: Serialize the objects into the Linked Art’s Provenance Model  
Conclusion:

Unfortunately, step 5 could not be complete as planned due to the lack of “Event” provenance in the metadata. As expressed in the above “project overview” and “note about Nazi-era Provenance,” information pertaining to the transfer of custody, acquisition, and object rediscovery is essential in creating  a JSON file from Linked Art’s Provenance Model. 


As noted in Step 3.1, once I realized there 

No specific art styles or movements were denoted, which could have been a signifier of Nazi-era pRovenance, as part of the cleansing had to do with surrealism, etc. 
