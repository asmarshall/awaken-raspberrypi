# import webbrowser
# import json
# import requests
# from pubnub import Pubnub
#
# r = requests.get('https://localhost:3000/devices/1')
# r.json()

import json, requests

url = 'http://localhost:3000/devices/1'

resp = requests.get(url=url)
data = json.loads(resp.text)

print data["message"]
