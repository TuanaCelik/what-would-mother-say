import requests
from haystack.nodes import BaseComponent

class TwitterRetriever(BaseComponent):
    outgoing_edges = 1
    
    def __init__(self, bearer_token: str, last_k_tweets: int = 10):
        self.headers = {"Authorization": "Bearer {}".format(bearer_token)}
        self.last_k_tweets = last_k_tweets
        
    def run(self, query: str, last_k_tweets: int = None):
        if last_k_tweets is None:
            last_k_tweets = self.last_k_tweets

        url = f"https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={query}&count={last_k_tweets}"
        try:
            response = requests.request("GET", url, headers=self.headers)
            twitter_stream = ""
            for tweet in response.json():
                print(tweet)
                twitter_stream += tweet["text"] + '\n'
        except Exception as e:
            twitter_stream = ["Please make sure you are providing a correct, public twitter account"]
        
        output = {
            "results":  f"{twitter_stream}",
            "username": query,
        }
        return output

    def run_batch(self):
        pass