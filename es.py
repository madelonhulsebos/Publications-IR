#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# sudo mongod --dbpath ~/Documents/Universiteit/2016-2017/P3_IR/Proj/pub/
# ./Documents/Universiteit/2016-2017/P3_IR/Proj/elasticsearch-5.2.2/bin/elasticsearch

import os, sys
import json
import pymongo
from pymongo import MongoClient
import pprint
from subprocess import call
import requests
from elasticsearch import Elasticsearch

# Initialise MongoDB connections
client = MongoClient()
db = client['Publications']
collection = db['pub']

# Initialise ElasticSearch
res = requests.get('http://localhost:9200')
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])	

# Export documents from MongoDB
# call("mongoexport --db Publications --collection pub --query '{\"journal\": \"IJCLCLP\"}' --out=test.json", shell=True)

# Open JSON file and append to list
# docs = []
# with open('test.txt', 'r') as open_file:
# 	for n in open_file:
# 		docs.append(json.loads(n))
# 	open_file.close()

# Index documents in ES instance
# for doc in docs:
# 	es.index(index="mm", doc_type="docs", id=doc.pop('_id'), body=doc)

def search(term):
	name = es.search(index="mm", body={ "query": { "match": { "year": str(term)}}})
	pprint.pprint(name['hits']['hits'])

# elastictest.index_docs(testjson)

search("2005")

