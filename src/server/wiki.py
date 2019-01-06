import boto3
import botocore
import wikipedia
from gensim import corpora

def pullEntryList(entry):
    # when typing a term, generate a list of possible queries

    list = wikipedia.search(entry, results=5)
        
    return list

def getLinks(query):
    # returns a list of links from the summary

    list = wikipedia.page(query).links

    return list

# def getCommonWords(query):
#     # get the most common words from the article
#     page = wikipedia.page(query).content

#     page = [x.encode('ascii') for x in page]

#     # remove common words and tokenize
#     stoplist = set('for a of the and to in'.split())
#     texts = [word for word in page.lower().split() if word not in stoplist]

#     # remove words that only appear once
#     from collections import defaultdict
#     frequency = defaultdict(int)
#     for text in texts:
#         for token in text:
#             frequency[token] += 1

#     texts = [[token for token in text if frequency[token] > 1]
#             for text in texts]

#     print(texts)

#     return texts