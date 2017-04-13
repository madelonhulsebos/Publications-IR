### To get it work properly first install the following items through Pip

 - requests
 - elasticsearch
 - flask
 - pymongo

### Run instructions

1. First start an instance of ElasticSearch using ./bin/elasticsearch in your elastic search folder.
2. Assuming you use the already populated elasticsearch instance, you can start the flask server by running python Userinterface_Elasticsearch/website.py. Otherwise run Userinterface_Elasticsearch/es.py with the MongoDB database running to build the elasticsearch index.
3. Go to localhost:5000 and the website should work.
