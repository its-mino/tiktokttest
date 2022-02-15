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
days_back = 2

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
    if len(list(videos)) > 0:
      for video in videos:
        try:
          total_views += video.info()['stats']['playCount']
          total_diggs += video.info()['stats']['diggCount']
          total_comments += video.info()['stats']['commentCount']
          total_shares += video.info()['stats']['shareCount']
        except:
          pass

      avg_views = total_views/len(list(videos))
      avg_diggs = total_diggs/len(list(videos))
      avg_comments = total_comments/len(list(videos))
      avg_shares = total_shares/len(list(videos))

      print(data['user']['nickname'], data['stats']['followerCount']+' followers', str(avg_views)+' avg views', str(avg_diggs)+' avg likes', str(avg_comments)+' avg comments', str(avg_shares)+' avg shares')
