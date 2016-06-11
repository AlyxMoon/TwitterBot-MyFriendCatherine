import tweepy
import re
import os

# Create the scheduler
from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler()

# Good ol' environment variables with our secret info
API_KEY = os.environ['API_KEY']
API_SECRET = os.environ['API_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

# Authentication and loading the API
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


def doTweet():
	# Search!
	result = api.search(q = '"my cat"', count = 1, rpp = 1, lang = 'en')
	text = result[0].text
	#text = 'my cat is a total square, my cat'

	# Filter out undesirable parts of string (such as mentions and urls)

	# Get rid of URL's completely
	text = re.sub('http\S+', '', text)
	# Remove mentions
	text = re.sub('@\S+', '', text)
	# Remove # and any text associated with them
	# Extra join and split is to remove resulting extra whitespace
	text = ' '.join(re.sub('#\S+', '', text).split())

	# Catherinize it
	pattern = re.compile('(?:^|\W)my cat(?:$|\W)', re.IGNORECASE)
	text = ' '.join(re.sub(pattern, ' my friend Catherine ', text).split())

	# It's done!
	print u'%s' % text
	api.update_status(text)

# Last but not least, schedule the task to run every 30 minutes
sched.addJob(doTweet, "Catherine-ize a Tweet", minutes = 30)