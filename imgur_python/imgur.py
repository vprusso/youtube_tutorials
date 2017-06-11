from credentials import CLIENT_ID
from credentials import CLIENT_SECRET
from imgurpython import ImgurClient

client_id = CLIENT_ID
client_secret = CLIENT_SECRET

client = ImgurClient(client_id, client_secret)

# Extracts the items (images) on the front page of imgur.
#items = client.gallery()
#for item in items:
#	print(item.link)
#	print(item.title)
#	print(item.views)
   
# Find the front page of imgur with highest views
#items = client.gallery()
#max_item = None
#max_views = 0
#for item in items:
#	if item.views > max_views:
#		max_item = item
#		max_views = item.views
#print(max_item.title)
#print(max_item.views)


