import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

responce = requests.get(url=url, params=params)
if responce.status_code == 200:
    responce_data = responce.json()  # get data in JSON format
    photos = responce_data['photos']  # get list of photos (dict)
    for photo in photos:
        photo_url = photo['img_src']  # get URL for a photo
        id_ = photo['id']  # get id for a photo
        responce = requests.get(photo_url)
        if responce.status_code == 200:
            # save photo locally
            with open(f'mars_rover_{id_}.jpg', 'wb') as file:
                file.write(responce.content)
        else:
            print('Error. Status code: ', responce.status_code)
else:
    print('Error. Status code: ', responce.status_code)

# with open('mars_rover.jpg', 'wb') as file:
#     file.write(responce.content)

# photos = responce_data['photos']
