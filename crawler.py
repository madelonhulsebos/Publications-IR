import requests
import json
subcategory_url = 'https://en.wikipedia.org/w/api.php?action=query&format=json&list=categorymembers&cmnamespace=14&cmlimit=500&cmtitle=Category:Algorithms'
r = requests.get(subcategory_url)
subcategories = json.loads(r.text)
# print(subcategories)
categorymembers = subcategories['query']['categorymembers']
# print(categorymembers)

seed_url = 'https://en.wikipedia.org/w/api.php?action=query&format=json&list=categorymembers&cmnamespace=0&cmlimit=500&cmtitle='
categories = []
def build_url(catmems):
    for catmem in catmems:
        page = {}
        page['Category'] = catmem['title'][9:]
        url = seed_url + catmem['title']
        page['URL'] = url
        categories.append(page)
        
build_url(categorymembers)
# print(categories)

#Downloading entire Web Document
def download_page(url):
    try:
        req = requests.get(url)
        respData = json.loads(req.text)
        return respData['query']['categorymembers']
    except Exception as e:
        print(str(e))

# Get all related algorithms for each category
def get_algorithms(categories):
    count = 0
    for category in categories:
        respData = download_page(category['URL'])
        category['Algorithms'] = respData
        count += len(respData)
    return count
number_of_algorithms = get_algorithms(categories)
# print(number_of_algorithms, categories)

# create abbreviations for algorithms with leading letters
def create_abbreviations(line):
    return ''.join(w[0].upper() for w in line.split())

def add_abbreviations(categories):
    for category in categories:
        for algorithm in category['Algorithms']:
            algorithm['abbreviation'] = create_abbreviations(algorithm['title'])
add_abbreviations(categories)

# write result to a json file
result = {}
result['categories'] = categories
with open('categories.json', 'w') as outfile:
    json.dump(result, outfile)