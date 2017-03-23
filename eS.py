class ES_integration:
	""" 
		Class function for using a ElasticSearch instance. 
	"""

	import requests
	from elasticsearch import Elasticsearch
	import json

	def search(self, uri, term):
	    """
	    	Simple Elasticsearch Query
	    """
	    # Returns results starting with prefix term
	    # Fuzzy allows for spelling mistakes to occur.
	    query = self.es.search(index="sw", body={"query": {"fuzzy_like_this_field" : {"like_text": str(term), "max_query_terms":5}}})
	    return query

	def searchExpressive(self):
		"""
			Probably some more expressive search queries.
		"""

	def format_results(self, results):
	    """
	    	Print results nicely:
	   			doc_id) content
	    """
	    data = [doc for doc in results['hits']['hits']]
	    for doc in data:
	        print("%s) %s" % (doc['_id'], doc['_source']['content']))

	def index_doc(self, uri, doctype):
	    """
	    	Index new documents to ElasticSearch instance.
	    """

	    doctype = "docs"

	    index = 1
	    while this.res.status_code == 200:
		    r = requests.get(str(uri)+str(index))
		    self.es.index(index="sw", doc_type=doctype, id=index, body=json.loads(r.content))
		    index = index + 1


	def __main__():
		"""
			eS elasticSearch Class Constructor
		"""
		self.res = requests.get('http://localhost:9200')
		self.es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

	if __name__ == '__main__':
		# execute only if run as the entry point into the program
		main()
