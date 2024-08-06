import requests
import json

base_url = 'http://127.0.0.1:8080/'
upload_endpoint = 'upload'
image_endpoint = 'image/'
delete_endpoint = 'delete/'


def upload_image(file_name):
    with open(file_name, 'rb') as file:
        # open file as image
        files = {'image': file}
        # make POST request to upload endpoint
        response = requests.post(base_url + upload_endpoint, files=files)
        # check response status code
        if response.status_code == 201:
            # handle the response from the server to extract image URL
            response_data = json.loads(response.text)
            image_url = response_data['image_url']
            print(f"image successfully uploaded: {image_url}")
        else:
            print(f"Invalid upload. Status code: {response.status_code}")


def download_image(file_name):
    # declare proper Content-Type for server to get uploaded image URL
    headers = {'Content-Type': 'text'}
    # make GET request to image endpoint
    response = requests.get(base_url + image_endpoint + file_name, headers=headers)
    # check response status code
    if response.status_code == 200:
        # handle the response from a server to extract uploaded image URL
        response_data = json.loads(response.text)
        uploaded_image_url = response_data['image_url']
        print(f"uploaded image url: {uploaded_image_url}")
    else:
        print(f"Error. Status code: {response.status_code}")


def delete_uploaded_image(file_name):
    # make DELETE request to delete endpoint
    response = requests.delete(base_url + delete_endpoint + file_name)
    # check response status code
    if response.status_code == 200:
        # handle the response from the server to extract message from the server
        response_data = json.loads(response.text)
        response_message = response_data['message']
        print(response_message)
    else:
        print(f"Error. Status code: {response.status_code}")


upload_image('mars_rover_102693.jpg')
download_image('mars_rover_102693.jpg')
delete_uploaded_image('mars_rover_102693.jpg')
