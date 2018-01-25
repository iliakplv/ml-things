import json


def get_non_null(s):
    return s if s is not None else ''


DOC_FILE = 'data/docs1.json'

with open(DOC_FILE) as doc_file:
    docs = json.load(doc_file)

titles = []
bylines = []
bodies = []

for doc in docs:
    title = get_non_null(doc['title'])
    byline = get_non_null(doc['byline'])
    body = get_non_null(doc['body'])

    titles.append(title)
    bylines.append(byline)
    bodies.append(body)

print('Docs total: {}'.format(len(docs)))
