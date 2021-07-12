from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer
import json #for easier data manipulation in the end

#some information is obscured by '*' the script will run if own inputs are set respectively
#mainly twitter dav auth tokens and the app key as well as the used IP

#Just for authorizsation
access_token = "9****960-*****************************************"
access_token_secret = "4K2*****************************e6DJx******"

# tweepy library to authenticate our API keys
api_key = "0********MDxxh**********"
api_secret = "O*************ZGZXoN91cTz**********imB*****"

#function in class that 'listens' for the kafka topic and writes data in json format to it
class StdOutListener(StreamListener):
    def on_data(self, data):
        json_ = json.loads(data) 
        producer.send("doge", data.encode('utf-8'))
        return True

    def on_error(self, status):
        print (status)

#listens to ip which is given in the server.properties file as well as here in link to the kafak topic
producer = KafkaProducer(bootstrap_servers='192.168.***.***:9092')
l = StdOutListener()

#twitter authorisation keys
auth = OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

#Data that should be scanned for in streamed twitter feeds
stream = Stream(auth, l)
stream.filter(track=["doge-coin", "doge", "doge-crypto"])





