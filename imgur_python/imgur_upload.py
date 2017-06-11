'''
	Here's how you upload an image. For this example, put the cutest picture
	of a kitten you can find in this script's folder and name it 'Kitten.jpg'
	For more details about images and the API see here:
		https://api.imgur.com/endpoints/image
'''

# Pull authentication from the auth example (see auth.py)
from auth import authenticate

from datetime import datetime

album = None # You can also enter an album ID here
image_path = 'a_7sus2.png'

def upload_image(client):
	'''
		Upload a picture.
	'''

	# Here's the metadata for the upload. All of these are optional, including
	# this config dict itself.
	config = {
		'album': album,
		'name':  'Ukulele Chords',
		'title': 'A 7sus2 Chord',
		'description': 'Chord chart generated: {0}'.format(datetime.now())
	}

	print("Uploading image... ")
	image = client.upload_from_path(image_path, config=config, anon=False)
	print("Done")
	print()

	return image


# If you want to run this as a standalone script
if __name__ == "__main__":
	client = authenticate()
	image = upload_image(client)

	print("Image was posted!")
	print("You can find it here: {0}".format(image['link']))