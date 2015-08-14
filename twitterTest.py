from TwitterAPI import TwitterAPI
import io
api = TwitterAPI('Consumer Key aka API key', 'Consumer Secret aka API Secret', 'Access Token', 'Access Token Secret')

r = api.request('statuses/filter', {'track':'pizza'})

try:
	for item in r:
		log = io.open(r'TweetFolder/tweets.txt','w', encoding='utf-8')
		log.write(item['text'])
		if('media' in item['entities']):
			log.write(u'\n--secretpasssword710--')
			log.write(item['entities']['media'][0]['media_url'])
		log.close()
		
except KeyboardInterrupt:
	log.close()
