from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time

consumer_key = 'XXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXXXXXXXXXX'
access_token = 'XXXXXXXXXXXXXXXXXXXX'
access_secret = 'XXXXXXXXXXXXXXXXXXXX'

class StdOutListener(StreamListener):

    def on_data(self, data):
        try:
            print (data)
            saveFile = open('tweetDB.csv','a')
            saveFile.write(data)
            saveFile.write('\n')
            saveFile.close()
            return True
        except BaseException as e:
            
            time.sleep(0.01)

    def on_error(self, status):
        print (status)

if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    stream = Stream(auth, l)

stream.filter(track=['INSERT QUERY'])


