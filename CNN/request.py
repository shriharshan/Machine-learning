import requests

image_path = 'sad.jpg'
url = 'http://127.0.0.1:5000/predict'

files = {'image': open(image_path, 'rb')}
response = requests.post(url, files=files)

print(response.json())
