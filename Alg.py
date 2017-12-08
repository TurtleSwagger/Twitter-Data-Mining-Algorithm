from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time

consumer_key = 'XwpDx9d9wn959MrUkLBHF4zRd'
consumer_secret = 'PnXqHE9SXRte55bM1RLmFjAdEPq51nwdNNSLplJAfCeJLJ9wJ7'
access_token = '486590450-lXLlOU6jxp5xc6uVVWUoldOAQuZwbfLdlSaasVbc'
access_secret = 'vOkzuIn1D9PoL10uX4l5nCZvzvtJBwh3TG8QlzWLouxKf'

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


