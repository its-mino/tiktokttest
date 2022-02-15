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
    print(data['user']['nickname'], data['stats']['followerCount'])
