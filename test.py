from TikTokApi import TikTokApi
api = TikTokApi()
search_term = "funny"
hashtag = api.hashtag(name=search_term)
for video in hashtag.videos():
  print(video)
