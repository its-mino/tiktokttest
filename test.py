from TikTokApi import TikTokApi
api = TikTokApi()
search_term = "funny"
hashtag = api.hashtag(name=search_term)
print(hashtag.info())