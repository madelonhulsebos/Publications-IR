#!/usr/bin/python
# -*- coding: utf-8 -*

from flask import Flask
from flask import request
from flask import url_for
import os, sys
import json
import pymongo
from pymongo import MongoClient
import pprint
from subprocess import call
import requests
from elasticsearch import Elasticsearch

# Initialise ElasticSearch
res = requests.get('http://localhost:9200')
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])	

app = Flask(__name__)

with open('categories.json', 'r') as open_file:
	# for n in open_file:
	algofile = json.load(open_file)
	open_file.close()

# Search for the paragraphs using the full term for the concept of method
def search_by_paragraph_term_and_abbrev(term, term2):
	t1 = term.encode(encoding="utf-8", errors="strict")
	t2 = term2.encode(encoding="utf-8", errors="strict")
	q = es.search(index="mm", body={
		"_source":["content.abstract", "title", "_id"],  
		"query": { "match_phrase": { "content.chapters.paragraphs": [t1, t2]}},
		"size":  40
		})

	return q

def search_by_paragraph_term(term):
	t1 = term.encode(encoding="utf-8", errors="strict")
	q = es.search(index="mm", body={
		"_source":["content.abstract", "title", "_id"],  
		"query": { "match_phrase": { "content.chapters.paragraphs": t1}},
		"size":  40
		})

	return q

def search_title(title):
	q = es.search(index="mm", body={
		"_source":["content.abstract", "content.fulltext", "title", "year", "journal"],  
		"query": { "match_phrase": { "_id": title.encode(encoding="utf-8", errors="strict")}},
		"size":  40
		})

	return q

# Get the abbreviated term
def get_abbrev(term):
	for n in algofile['categories']:
		for o in n['Algorithms']:
			if term == o['title']:
				return o['abbreviation']

search_bar = """
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/spacelab/bootstrap.min.css">

<!-- Latest compiled and minified JavaScript -->
<script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>

<title>MethodMiner</title>
    
<nav class="navbar navbar-default">
	<div class="container-fluid">
		<div class="row">
			<div class="col-md-4">
				<img src="http://i.imgur.com/1ZDqtLD.png" style="margin:1.2em 1em;">
			</div>
			<div class="col-md-8">
				<form action="/" method="post" class="navbar-form navbar-right" role="search">
				    <div class="input-group">
				        <input name="query" type="text" class="form-control" placeholder="Search" style="width:40em; max-width:100%; margin:1.8em 1em;">
				        <div class="input-group-btn">
				            <button type="submit" class="btn btn-default">
				                <span class="glyphicon glyphicon-search" aria-hidden="true"></span>
				            </button>
				        </div>
				    </div>
				</form>
			</div>
		</div>
	</div>
</nav>
	"""
table_doc_begin = 	"""
				<div class="panel panel-default">
		  		<!-- Default panel contents -->

				<!-- Table -->
				<table class="table-striped table-condensed">
				    <col width="15%" />
					<col width="84%" />
				"""

table_begin = 	"""
				<div class="panel panel-default">
		  		<!-- Default panel contents -->

				<!-- Table -->
				<table class="table-striped table-condensed">
				    <col width="30%" />
					<col width="69%" />
					<tr>
						<th><h3>Title</h3></th>
						<th><h3>Abstract</h3></th> 
					</tr>
				"""

table_end = """
			</table>
			</div>
			"""

@app.route('/', methods=['GET', 'POST'])
# @app.route('/')
def searchpage():
	if request.method == 'POST':
		term = request.form['query'].encode(encoding="utf-8", errors="strict")

		if get_abbrev(term) is not None:
			q = search_by_paragraph_term_and_abbrev(term, get_abbrev(term).encode(encoding="utf-8", errors="strict"))
		else:
			q = search_by_paragraph_term(term)
		
		show_term = """<h3>Showing results for query: <em>"""+term+"""</em></h3>"""

		string = show_term + table_begin

		try:
			for lines in q['hits']['hits']:
				
				# TEST
				# return str(lines)
				title_text = lines['_source']['title'].encode(encoding="utf-8", errors="strict")
				id_text = lines['_id'].encode(encoding="utf-8", errors="strict")
				abstract_text = lines['_source']['content']['abstract'].encode(encoding="utf-8", errors="strict")

				if len(abstract_text) > 350:
					abstract_text = abstract_text[0:349]

				if title_text is not None:
					if abstract_text is not None:
						if id_text is not None:
							
							link = 	"""
									<a href=" """+id_text+""" ">
										"""+title_text+"""
									</a>
									"""
							
							table_item = """
										<tr>
											<th>
												"""+link+"""
											</th>
											<td>"""+abstract_text+"""...</td> 
										</tr>
										"""

							string = string + table_item
							
			string + table_end
			return search_bar + string
		except Exception:
			return search_bar + """Caught Exception"""
	else:
		return search_bar

@app.route('/<doc_title>', methods=['GET'])
def document_page(doc_title):
	q = search_title(doc_title)
	try:
		for lines in q['hits']['hits']:
			# DEBUG
			# return str(lines)
			
			title_text = lines['_source']['title'].encode(encoding="utf-8", errors="strict")
			journal = lines['_source']['journal'].encode(encoding="utf-8", errors="strict")
			year = lines['_source']['year'].encode(encoding="utf-8", errors="strict")
			abstract_text = lines['_source']['content']['abstract'].encode(encoding="utf-8", errors="strict")
			paragraphs = lines['_source']['content']['fulltext'].encode(encoding="utf-8", errors="strict")

			if title_text is not None:
				if abstract_text is not None:
					if year is not None:
						if journal is not None:
							if paragraphs is not None:

								title_text = """<h3>""" + title_text + """</h3><br>"""
								
								table_item = """
											<tr>
												<th>
													Year
												</th>
												<td>"""+year+"""</td> 
											</tr>
											<tr>
												<th>
													Journal
												</th>
												<td>"""+journal+"""</td> 
											</tr>
											<tr>
												<th>
													Abstract
												</th>
												<td>"""+abstract_text+"""</td> 
											</tr>
											<tr>
												<th>
													Paragraphs
												</th>
												<td>"""+paragraphs+"""</td> 
											</tr>
											"""

		return search_bar + title_text +table_doc_begin + table_item + table_end
	except Exception:
		pprint.pprint(Exception)

if __name__ == '__main__':
    app.run()