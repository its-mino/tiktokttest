from TikTokApi import TikTokApi
api = TikTokApi()
search_term = "funny"
hashtag = api.hashtag(name=search_term)
authors = []
for video in hashtag.videos():
  authors.append(video.author)

for author in authors:
  print(author.info_full())
