from TikTokApi import TikTokApi
import datetime
import time

api = TikTokApi()

#Settings
#hashtag to search
search_term = "gamergirl"
#how many videos to search in hashtag
num_videos = 500
#number of days to average user content metrics
days_back = 7

hashtag = api.hashtag(name=search_term)
authors = []
for video in hashtag.videos(count=num_videos):
  authors.append(video.author)

completed_authors = []
authors = list(authors)
for author in authors:
  if author.username not in completed_authors:
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
      list_videos = list(videos)
      number_of_videos = len(list_videos)
      added_vids = 0
      if number_of_videos > 0:
        for video in list_videos:
          try:
            total_views += video.info()['stats']['playCount']
            total_diggs += video.info()['stats']['diggCount']
            total_comments += video.info()['stats']['commentCount']
            total_shares += video.info()['stats']['shareCount']
            added_vids += 1
          except:
            pass

        avg_views = total_views/added_vids
        avg_diggs = total_diggs/added_vids
        avg_comments = total_comments/added_vids
        avg_shares = total_shares/added_vids

        print(author.username, data['stats']['followerCount'], 'followers | ', int(avg_views), 'avg views | ', int(avg_diggs), 'avg likes | ', int(avg_comments), 'avg comments | ', int(avg_shares), 'avg shares')
        completed_authors.append(author.username)
