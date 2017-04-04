from nltk.tag import StanfordNERTagger
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.metrics.scores import accuracy

### PUBLICATION TEXT PROCESSING

wordssplitted = []
# Split on word level
for sentence in sentences
	words = word_tokenize(sentence)
	wordssplitted.append([words])

# Stopword removal
filtered_sentences = []
stop_words = set(stopwords.words('english'))
for sentence in wordssplitted
	words = sentence
	for w in words:
		if w not in stop_words:
			filtered_sentences.append([w])

testfile = open(r'C:\Users\Madelon\Documents\Madelon\1. TU Delft\CS\1. MSc 1\Q3 Information Retrieval\Project\Trainingdata\Trainingdata.csv', 'wb')		
wr = csv.writer(testfile, quoting=csv.QUOTE_NONNUMERIC)			
			
# For the first trained model: train on stemmed sentences
ps = PorterStemmer()
stemmed_sentences = [] # Retrieve testset
for sentence in filtered_sentences:
	for s in sentence:
		stem_result = ps.stem(s)
		stemmed_sentence = stemmed_sentence + stem_result
	# Write this testset to a new file 
	stemmed_sentences.append([stemmed_sentence])
	wr.writerow(stemmed_sentence)
	stemmed_sentence = []
	
	
### CLASSIFICATION PART - TEST & EVALUATION	(Classifier trained using Java)
jar = 'C:/Users/Madelon/Downloads/stanford-ner/stanford-ner/stanford-ner.jar'

# Default model (Extracts persons, organizations, etc.)
model = 'C:/Users/Madelon/Downloads/stanford-ner/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz'
# Trained model on stemmed sentences
ownmodel_stemmed = 'C:/Users/Madelon/Downloads/stanford-ner/stanford-ner/classifiers/.......crf.ser.gz'
# Trained model on complete sentences
ownmodel_complete = 'C:/Users/Madelon/Downloads/stanford-ner/stanford-ner/classifiers/.......crf.ser.gz'

# Execute classifier on testset WITH STEMMING
stNER_stem = StanfordNERTagger(ownmodel_stemmed, jar, encoding='utf8')
classified_text_stem = stNER_stem.tag(stemmed_sentences)

# Execute classifier on testset WITHOUT STEMMING
stNER_complete = StanfordNERTagger(ownmodel_complete, jar, encoding='utf8')
classified_text_complete = stNER_complete.tag(sentences)

# Testing Stanford NER Tagger for accuracy
# Retrieve annotated sentences from test dataset
reference_annotations = []
accuracy = accuracy(reference_annotations, classified_text)