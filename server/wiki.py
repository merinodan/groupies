import boto3
import wikipedia

def pullEntryList(entry):
    # when typing a term, generate a list of possible queries

    list = wikipedia.search(entry, results=5)

    return list

def pullWikipediaPage(query):
    # pull the page from wikipedia

    summary = wikipedia.summary(query)

    return summary

def getLinks(summary):
    # returns a list of links from the summary

    list = summary

    return list