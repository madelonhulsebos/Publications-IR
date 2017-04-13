# Install elasticsearch dependencies using Anaconda: conda install -c conda-forge elasticsearch=5.2.0

import nltk
import re
import pprint
import requests
# First install package 'unicodecsv'
import unicodecsv as csv
from nltk import sent_tokenize
from elasticsearch import Elasticsearch
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
database = client['IRDB_pubs']

# Call total collection to retrieve publications of specific journals
collection = database['Publications']
subcollection = collection.find({'booktitle' : 'JCDL','booktitle' : 'TPDL','booktitle' : 'SIGIR', 'booktitle' :'TREC', 'booktitle' :'ECDL', 'booktitle' :'ICSE', 'booktitle' :'ESWC', 'booktitle' :'CWSM','booktitle' : 'VLDB', 'booktitle' :'WWW'})

# Stuff the subcollection with these journals
journalscollection = database['journalsCollection']
journalscollection.insert(subcollection)

methodcollection = database['methods']

# Create method collection (complete json file was added)
database.createCollection('methods')
db.getCollection('methods').insert([...]) # Other methods were added

# Zelfde voor algorithms
pubs = []
journalpubs = journalscollection.find({})
for pub in journalpubs:
    try:
        content = pub
        pubs.append(content)
    except:
        print("")
		
# Setup connection with elastic search
res = requests.get('http://localhost:9200')
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# Indexing the publications
for pub in pubs:
    es.index(index="mm", doc_type="pubs", id=pub.pop('_id'), body=pub)

# Search method to find paragraph of publications that mention a method
def search(term):
    q2 = es.search(index="mm", body={"_source":["content.chapters.paragraphs"], "query": {"match_phrase":{"content.chapters.paragraphs": str(term)}}, "size": 1000}) 
	return q2['hits']['hits']

es.indices.create(index=‘mm', ignore=400)

search("html")

# Retrieve all algorithm titles from the taxonomy
methodcollection = database['methods']
methodcollection = methodcollection.find({})
algorithmlist = []
for category in methodcollection:
	algorithmcollection = category['Algorithms']
	try:
		for algorithm in algorithmcollection:
			try:
				alg = algorithm['title']
				algorithmlist.append(alg)
				
			except:
				print("")
	except:
		print("")
	
# Check the publications subset for occurences of each algorithm from the taxonomy
algparagraphs = []
for algorithm in algorithmlist:
		algparagraph = search(algorithm)
		algparagraphs.append(algparagraph)

# Write paragraphs to 
myfile = open(r'C:\Users\Madelon\Documents\Madelon\1. TU Delft\CS\1. MSc 1\Q3 Information Retrieval\Project\Trainingdata\Trainingdata.csv', 'wb')		
wr = csv.writer(myfile, quoting=csv.QUOTE_NONNUMERIC)
# sentences = sent_tokenize(str(algparagraphs[:100]))
for algparagraph in algparagraphs:
	sentences= sent_tokenize(str(algparagraph))#re.split(r' *[\.\?!][\'"\)\]]* *', str(algparagraph))
	for sentence in sentences:
		for algorithm in algorithmlist:
			stringsentence = str(sentence)
			if algorithm in stringsentence:
				print(algorithm)
				print(sentence)
				wr.writerow([stringsentence])

	
