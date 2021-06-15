#Just for authorizsation
twitter_keys = {
    "consumer_key": "co7h6LYkJdomom3zo3IYngiXN",
    "consumer_secret": "<To be replace>",
}
 
# tweepy library to authenticate our API keys
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

#Rate limit reached --> exception for going past the rate limit
api = tweepy.API(
            auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True
       )

#Actual funtion for Datamining
def mine_crypto_currency_tweets(self, query="BTC"):

    last_tweet_id = False
    page_num = 1

    data = get_df()
    cypto_query = f"#{query}"
    print(" ===== ", query, cypto_query)
    for page in tweepy.Cursor(
        self.api.search,
        q=cypto_query,
        lang="en",
        tweet_mode="extended",
        count=200, 
    ).pages():
        print(" ...... new page", page_num)
        page_num += 1

        for item in page:
            mined = {
                "tweet_id": item.id,
                "name": item.user.name,
                "screen_name": item.user.screen_name,
                "retweet_count": item.retweet_count,
                "text": item.full_text,
                "mined_at": datetime.datetime.now(),
                "created_at": item.created_at,
                "favourite_count": item.favorite_count,
                "hashtags": item.entities["hashtags"],
                "status_count": item.user.statuses_count,
                "followers_count": item.user.followers_count,
                "location": item.place,
                "source_device": item.source,
            }

            try:
                mined["retweet_text"] = item.retweeted_status.full_text
            except:
                mined["retweet_text"] = "None"

            last_tweet_id = item.id
            data = data.append(mined, ignore_index=True)

        if page_num % 180 == 0:
            date_label = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            print("....... outputting to csv", page_num, len(data))
            data.to_csv(f"{query}_{page_num}_{date_label}.csv", index=False)
            print("  ..... resetting df")
            data = get_df()

    date_label = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    data.to_csv(f"{query}_{page_num}_{date_label}.csv", index=False)