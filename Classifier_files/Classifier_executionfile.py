from pymongo import MongoClient
import unicodecsv as csv

### PUBLICATION TEXT PROCESSING
client = MongoClient('mongodb://localhost:27017/')
database = client['IRDB_pubs']
collection = database['Publications']
	
# Trained the classifier with: 
# java -cp stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -prop train.prop

# Accuracy of trained classifier
#CRFClassifier tagged 8677 words in 288 documents at 5689,84 words per second.
#         Entity P       R       F1      TP      FP      FN
#              M 0,6694  0,1957  0,3028  81      40      333
#         Totals 0,6694  0,1957  0,3028  81      40      333

publications = collection.find({'journal':'I. J. Network Security'},{'journal':'IJCLCLP'})
testfile = open(r'C:\Users\Madelon\Documents\Madelon\1. TU Delft\CS\1. MSc 1\Q3 Information Retrieval\Project\Trainingdata\NewMethodsFile.csv', 'wb')
for pub in publications:
	fulltext = pub['content.fulltext']
	wr = csv.writer(testfile, quoting=csv.QUOTE_NONNUMERIC)	
	wr.writerow([fulltext])

# Executed the classifier on unseen publications
# From Stanford src folder, execute in command prompt (save empty OUTPUT_newmethods.csv in src folder first) :
# java -cp stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier train_final.ser.gz -textFile NewMethodsText.txt > OUTPUT_newmethods.csv
