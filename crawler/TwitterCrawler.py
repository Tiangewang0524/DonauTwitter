import json
from TwitterAPI import TwitterAPI
import TwitterSearch
import TwitterStream
import db
import sys

data = json.load(open('config.json'))


consumer_key = data["consumer_key"]
consumer_secret = data["consumer_secret"]
access_token_key = data["access_token_key"]
access_token_secret = data["access_token_secret"]
keywords = data["keywords"]

locations = data['locations']
geocode = data['geocode']

db=db.dbclient(data['db_url'],data['db_name'])

api = TwitterAPI(consumer_key,
                 consumer_secret,
                 access_token_key,
                 access_token_secret)

if sys.argv[1]=='s':
	TwitterSearch.search(api,db,keywords,geocode)
elif sys.argv[1]=='f':
	TwitterStream.search(api,db,keywords,locations)
else:
	print "Command not recognized"
