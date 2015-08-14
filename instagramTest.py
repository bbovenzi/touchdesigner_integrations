from instagram import InstagramAPI
import io

api = InstagramAPI(client_id='CLIENT_ID', client_secret='CLIENT_SECRET')

log = io.open(r'InstagramFolder/instagram.txt','wb')
hashtags = ['pizza','cheese'] #add as many search terms you need here
lat = 38.907192 
long = -77.036871
dist = 1000 #in meters

# Search location by long+lat

def search_by_lat_long(latitude, longitude, distance):
	media_search = api.media_search(lat=latitude,lng=longitude, distance=distance)
	for media in media_search:
		log.write(u'\n--&&&***--')
		log.write(media.user.username + ' ')
		if(media.caption):
			log.write(media.caption.text.encode('utf8') + '---')
		if(media.location):
			log.write(media.location.name + ' ')
		if(media.images):
			log.write(media.images['standard_resolution'].url)
		elif(media.videos):
			log.write(media.videos['standard_resolution'].url)

# Search by hashtag

def search_by_hashtag(hashtags):
	for hashtag in hashtags:
		tag_recent_media = api.tag_recent_media(tag_name=hashtag)
		for media in tag_recent_media[0]:
			log.write(u'\n--&&&***--')
			log.write(media.user.username + ' ')
			if(media.caption):
				log.write(media.caption.text.encode('utf8') + '---')
			#if(media.location):
			#	log.write(media.location.name + ' ')
			if(media.images):
				log.write(media.images['standard_resolution'].url)
			elif(media.videos):
				log.write(media.videos['standard_resolution'].url)

'''
# Search by user
def search_by_user():
	access_token = "(u'429379349.e9294d5.f7f0376b87bd43bbb5c3112e7c8ed5d1', {u'username': u'bbovenzi', u'bio': u'', u'website': u'http://bbovenzi.com', u'profile_picture': u'https://instagramimages-a.akamaihd.net/profiles/profile_429379349_75sq_1371916365.jpg', u'full_name': u'Brent Bovenzi', u'id': u'429379349'})"

	username = 'bbovenzi'

	user_recent_media = api.user_recent_media(user_id=username, count=10)
	for media in user_recent_media:
		log.write(u'\n--&&&***--')
		log.write(media.user.username + ' ')
		if(media.caption):
			log.write(media.caption.text.encode('utf8') + '---')
		if(media.location):
			log.write(media.location.name + ' ')
		if(media.images):
			log.write(media.images['standard_resolution'].url)
		elif(media.videos):
			log.write(media.videos['standard_resolution'].url)

search_by_user()
'''
#---------------------------------------------------------------------------------------------------------------------
#search_by_lat_long(lat, long, dist)
search_by_hashtag(hashtags)
log.close()