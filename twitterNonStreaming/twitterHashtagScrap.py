from twython import Twython
import threading

TWITTER_APP_KEY = 'xxxxxxxxxxxx'
TWITTER_APP_KEY_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx' 
TWITTER_ACCESS_TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'
TWITTER_ACCESS_TOKEN_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'

def fun():
	t = Twython(app_key=TWITTER_APP_KEY, 
            app_secret=TWITTER_APP_KEY_SECRET, 
            oauth_token=TWITTER_ACCESS_TOKEN, 
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

	search = t.search(q='#MakeInIndia', count=50)

	tweets = search['statuses']

#Error : UnicodeEncodeError: 'ascii' codec can't encode character u'\u2026' .encode(utf-8)

	for tweet in tweets:
  		print tweet['id_str'], '\n', tweet['text'].encode('utf-8'), '\n\n\n'



def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

set_interval(fun, 60)

