# YouTube Videos:
# Part 1: https://www.youtube.com/watch?v=OiDQu-0-DIA
# Part 2: https://www.youtube.com/watch?v=kDcn_Tn-ti8
# Part 3: https://www.youtube.com/watch?v=MyCr8kPT3OI
import configparser

from imgurpython import ImgurClient

config = configparser.ConfigParser()
config.read('auth.ini')

client_id = config.get('credentials', 'client_id')
client_secret = config.get('credentials', 'client_secret')

client = ImgurClient(client_id, client_secret)

# Extracts the items (images) on the front page of imgur.
items = client.gallery()
for item in items:
    print(item.link)
    print(item.title)
    print(item.views)

# Find the front page of imgur with highest views
#items = client.gallery()
#max_item = None
#max_views = 0
#for item in items:
#   if item.views > max_views:
#       max_item = item
#	max_views = item.views
#print(max_item.title)
#print(max_item.views)


