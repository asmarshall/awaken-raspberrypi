#!/usr/bin/python
#!/usr/bash
import webbrowser
import json, requests
from pubnub import Pubnub


pubnub = Pubnub(
        subscribe_key = 'sub-c-e99cc9a0-1bce-11e7-a9ec-0619f8945a4f',
        publish_key = 'pub-c-0a1d95bd-193e-4483-84ae-737d39abf8f2')

channel = "my_channel"

def callback(message, channel):
    print('[' + channel + ']: ' + str(message))
    settv(message.get("action"))
    loadpage(message.get("url"))

pubnub.subscribe(
        channel,
        callback = callback)

def loadpage(url):
  import os
  import webbrowser
  import shlex, subprocess

  urltrue = url
  os.system("export DISPLAY=:0.0")
  os.system("pkill chromium & ; sleep 2")
  os.system("chromium --kiosk %s" % urltrue)
def settv(check):
  if check == False:
    import os
    os.system("date")
    os.system('echo "standby 0" | cec-client -s -d 1')

  elif check == True:
    import os
    os.system("date")
    os.system('echo "on 0" | cec-client -s -d 1')

