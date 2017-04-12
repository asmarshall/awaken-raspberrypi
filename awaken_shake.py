import webbrowser
import json
import requests
from pubnub import Pubnub

r = requests.get('https://localhost:3000/devices/1')
r.json()
