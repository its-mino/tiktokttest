from TikTokApi import TikTokApi
import datetime
import time

api = TikTokApi()

#Settings
#hashtag to search
search_term = "funny"
#how many videos to search in hashtag
num_videos = 30
#number of days to average user content metrics
days_back = 5

hashtag = api.hashtag(name=search_term)
authors = []
for video in hashtag.videos(count=num_videos):
  authors.append(video.author)

for author in authors:
  data = author.info_full()
  if data['stats']['followerCount'] >= 250000 and data['stats']['followerCount'] < 1500000:
    total_views = 0
    total_diggs = 0
    total_comments = 0
    total_shares = 0
    now = datetime.datetime.now()
    then = now - datetime.timedelta(days=days_back)
    then = time.mktime(then.timetuple())
    videos = author.videos(cursor=then)
    number_of_videos = len(list(videos))
    if number_of_videos > 0:
      for video in videos:
        print(video.info())
        total_views += video.info()['stats']['playCount']
        total_diggs += video.info()['stats']['diggCount']
        total_comments += video.info()['stats']['commentCount']
        total_shares += video.info()['stats']['shareCount']

      avg_views = total_views/number_of_videos
      avg_diggs = total_diggs/number_of_videos
      avg_comments = total_comments/number_of_videos
      avg_shares = total_shares/number_of_videos

      print(data['user']['nickname'], data['stats']['followerCount'], 'followers', avg_views, 'avg views', avg_diggs, 'avg likes', avg_comments, 'avg comments', avg_shares, 'avg shares')
