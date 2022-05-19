import requests
import sys

def get_comments(video_id):
    # Gets only 100 comments
    # Can't understand the algo filtering comments. Not all of them shown.
    url = 'https://www.googleapis.com/youtube/v3/commentThreads'
    params = {
        'key': 'AIzaSyA6AEpVsV8NufvqVcyCw2EhIs9QaOmdduM',
        'part': 'snippet',
        'videoId': video_id,
        'maxResults': 100,
        'order': 'relevance'
    }
    items_from_response = requests.get(url, params=params).json()['items']
    comments = [
        item['snippet']['topLevelComment']['snippet']['textDisplay']
        for item in items_from_response
    ]
    return comments

if __name__ == '__main__':
    video_id = sys.argv[1]
    for comment in get_comments(video_id):
        print(comment, end='\n\n') # Two new lines for better readability
