#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

class testNaam:
	""" 
		Class function for using a ElasticSearch instance. 
		
		Author: Wesley Quispel
		Student Number: 4014901

		Last updated: 2017-04-01
		
		Usage:
			
			Initialise:
			elastic = ES_integration()
			
			Clear previous MongoDB if database is updated:
			elastic.clear_index(name) TODO

			Populate from MongoDB:
			elastic.index_docs(name, jsonvariable) TODO

			Search queryterm:			
			res = elastic.search(queryterm) TODO
				@returns: list of n results consisting of sentences from the full text of the publications.
	"""

	def __init__ (self):
		import requests
		from elasticsearch import Elasticsearch
		import elasticsearch.helpers as ESH
		import json
		
		# Name under which data is indexed
		self.index_name = "mm"

		# Amount of results for a query
		self.query_returns = 5

		# Document type name
		self.doc_type_name = "docs"

		self.res = requests.get('http://localhost:9200')
		self.es = Elasticsearch([{'host': 'localhost', 'port': 9200}])	

	# __________________________________METHODS________________________________________________________________


	def search(self, term):
		"""
			Simple Elasticsearch Query

			"number_of_fragments" : 1
		"""
		# results = []
		query_results =  self.es.search(index=self.index_name, body={"query": {"query_string": {"query":term}, "fields":["fulltext", "paragraphs", "_id", "title"]}, "number_of_fragments" : 1})
		# for r in query_results:
		# 	for n in r:
		# 		if n.find(term):
		return query_results

	def clear_index(self):
		"""
			Clear the old index if new items need to be added. Call index_docs afterwards.
		"""
		self.es.delete(index=self.index_name)


	def index_docs(self, json_file):
		"""
			Index new documents to ElasticSearch instance.
		"""
		self.es.index(index=self.index_name, doc_type=self.doc_type_name, id=1, body=json_file)

		# self.ESH.bulk(self.es, json_file, index=self.index_name, doc_type=self.doc_type_name)
