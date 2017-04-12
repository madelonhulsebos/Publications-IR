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
# client = MongoClient()
# db = client['Publications']
# collection = db['pub']

# Initialise ElasticSearch
res = requests.get('http://localhost:9200')
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])	

# Create an ElasticSearch index for the first run.
# es.indices.create(index='my-index', ignore=400)

# # Export documents from MongoDB
# call("mongoexport --db Publications --collection pub --query '{\"journal\": \"IJCLCLP\"}' --out=pubs.json", shell=True)

# # Open JSON file and append to list
# docs = []
# with open('pubs.json', 'r') as open_file:
# 	for n in open_file:
# 		docs.append(json.loads(n))
# 	open_file.close()

# # Index documents in ES instance
# for doc in docs:
# 	es.index(index="mm", doc_type="docs", id=doc.pop('_id'), body=doc)

with open('categories.json', 'r') as open_file:
	# for n in open_file:
	algofile = json.load(open_file)
	open_file.close()


# Search for the paragraphs using the full term for the concept of method
def search_by_paragraph_term(term):
	q = es.search(index="mm", body={
		"_source":["content.chapters.paragraphs"],  
		"query": { "match_phrase": { "content.chapters.paragraphs": str(term)}},
		"size":  40
		})

	return q


# Search for the titles containing mentions of the term
def search_for_title(term):
	q = es.search(index="mm", body={
		"_source":["title"],
		"query": { "match_phrase": {"content.chapters.paragraphs": str(term)}},
		"size":  40
		})

	res = []
	for n in q['hits']['hits']:
		res.append(n['_source']['title'])
	
	return res


# Search for the paragraphs using the abbreviation for the concept of method
def search_by_paragraph_abbrev(term, titles):
	res = []
	q = es.search(index="mm", body={
		"_source":["content.chapters.paragraphs", "title"],  
		"query": { "match_phrase": { "content.chapters.paragraphs": str(term)}},
		"size":  40
		})
	
	for doc in q:
		# pprint.pprint(doc)
		for n in doc:
			pprint.pprint(n)
		# 	if n['title'] == title:
		# 		res.append(n)

	pprint.pprint(res)


# Get the abbreviated term
def get_abbrev(term):
	for n in algofile['categories']:
		for o in n['Algorithms']:
			if term == o['title']:
				return o['abbreviation']


# Search for a term
def search_comprehensive(term):
	# Retrieve abbreviation for term
	abbrev = get_abbrev(term)
	
	titles = search_for_title(term)
	paras_term = search_by_paragraph_term(term)
	paras_abbrev = search_by_paragraph_abbrev(abbrev, titles)

	pprint.pprint(paras_abbrev)


search_comprehensive('The prosodic features related to pitch and energy failed to distinguish the valence emotions. The selected features discussed in Section 3.1 were quantized into feature vector 1 Y and mean feature vector 2 Y')
