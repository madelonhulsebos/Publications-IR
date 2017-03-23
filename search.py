
# make sure ES is up and running
import requests
res = requests.get('http://localhost:9200')
print(res.content)

#connect to our cluster
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

#let's iterate over swapi people documents and index them
import json
r = requests.get('http://localhost:9200') 
i = 1
while r.status_code == 200:
    r = requests.get('http://swapi.co/api/people/'+ str(i))
    es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content))
    i=i+1
 
print(i)

es.get(index='sw', doc_type='people', id=5)

# r = requests.get('http://localhost:9201')
# i = 18
# while r.status_code == 200:
#    r = requests.get('http://swapi.co/api/people/'+ str(i))
#    es.index(index='sw', doc_type='people', id=i,     body=json.loads(r.content))
#    i=i+1


# print(str(es.search(index="sw", body={"query": {"match": {'name':'Darth Vader'}}}).values()[2]) + "\n")
res = es.search(index="sw", body={"query": {"match": {'name':'Darth Vader'}}})
print(res['hits']['hits'])
# print(str(es.search(index="sw", body={"query": {"match": {'name':'Darth Vader'}}})) + "\n")
# print(str(es.search(index="sw", body={"query": {"prefix" : { "name" : "lu" }}})))
# print(str(es.search(index="sw", body={"query":{"fuzzy_like_this_field":{"name":{"like_text":"jaba","max_query_terms":5}}}})))


def search(uri, term):
    """Simple Elasticsearch Query"""
    query = json.dumps({
        "query": {
            "match": {
                "content": term
            }
        }
    })
    response = requests.get(uri, data=query)
    results = json.loads(response.text)
    return results

def format_results(results):
    """Print results nicely:
    doc_id) content
    """
    data = [doc for doc in results['hits']['hits']]
    for doc in data:
        print("%s) %s" % (doc['_id'], doc['_source']['content']))

def create_doc(uri, doc_data={}):
    """Create new document."""
    query = json.dumps(doc_data)
    response = requests.post(uri, data=query)
    print(response)



# from elasticsearch import Elasticsearch
 
es = Elasticsearch()
res = es.search(index="test", doc_type="articles", body={"query": {"match": {"content": "fox"}}})
print("%d documents found" % res['hits']['total'])
for doc in res['hits']['hits']:
    print("%s) %s" % (doc['_id'], doc['_source']['content']))

es.create(index="test", doc_type="articles", body={"content": "One more fox"})