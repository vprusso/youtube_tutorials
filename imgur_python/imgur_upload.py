from auth import authenticate
from datetime import datetime

album = None
image_path = 'a_7sus2.png'

def upload_image(client):
	"""
	Uploads and image to imgur
	"""

	config = {
		'album': album,
		'name': 'Ukulele Chords',
		'title': 'A 7sus2 Chord',
		'description': 'Chord chart generated: {0}'.format(datetime.now())
	}

	print('Uploading image...')
	image = client.upload_from_path(image_path, config=config, anon=False)
	print("Done")
	print()

	return image

if __name__ == "__main__":
	client = authenticate()
	image = upload_image(client)

	print("Image was posted!")
	print("You can find the image here: {0}".format(image['link']))