import requests
import ctypes

def get_token():
    with open('.token', 'r') as file:
        token = file.readline()
        return token.strip()

def get_img():
    token = get_token()
    req = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={token}&count=1')
    json = req.json()

    while json[0]['media_type'] == 'video':
        req = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={token}&count=1')
        json = req.json()
    return requests.get(json[0]['url']).content

with open('img.jpg', 'wb') as file:
    file.write(get_img())

ctypes.windll.LoadLibrary('user32.dll').SystemParametersInfoW(20, 0, "d:/apod/img.jpg" , 0)