from TikTokApi import TikTokApi
api = TikTokApi()

#Settings
search_term = "funny"
num_videos = 30


hashtag = api.hashtag(name=search_term)
authors = []
for video in hashtag.videos(count=num_videos):
  authors.append(video.author)

for author in authors:
  data = author.info_full()
  if data['stats']['followerCount'] >= 250000 and data['stats']['followerCount'] < 1500000:
    total_views = 0
    for video in author.videos():
      print(video.info())
      total_views += video.info()['stats']['playCount']
      avg_views = total_views/10
    print(data['user']['nickname'], data['stats']['followerCount'], avg_views)
