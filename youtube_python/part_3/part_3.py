import json
import re
import urllib.request

from pytube import YouTube

class Helper:
    def __init__(self):
        pass

    def title_to_underscore_title(self, title: str):
        title = re.sub('[\W_]+', "_", title)
        return title.lower()

    def id_from_url(self, url: str):
        return url.rsplit("/", 1)[1]

api_key = "PUT YOUR API KEY IN HERE"

s = "https://youtu.be/C0PuCgQrxZU"
t = "Neural Networks in Python: Part 1 -- Part A"
helper = Helper()
print(helper.id_from_url(s))
print(helper.title_to_underscore_title(t))
#video_id = "C0PuCgQrxZU"
#url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}"

#json_url = urllib.request.urlopen(url)
#data = json.loads(json_url.read())

#print(data)
