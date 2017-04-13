
import json, requests
from pubnub import Pubnub

def getserial():
  # Extract serial from cpuinfo file
  cpuserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
  except:
    cpuserial = "ERROR000000000"

  return cpuserial


url = "http://localhost:3000/devices/connect/%s" % getserial();

resp = requests.get(url=url)
data = json.loads(resp.text)
pschannel = data["channel"]
psurl = data["url"]
loadpage(psurl);

pubnub = Pubnub(
        subscribe_key = 'sub-c-e99cc9a0-1bce-11e7-a9ec-0619f8945a4f',
        publish_key = 'pub-c-0a1d95bd-193e-4483-84ae-737d39abf8f2')

channel = pschannel

def callback(message, channel):
    settv(message.get("action"))
    loadpage(message.get("url"))

def settv(check):
  if check == False:
    import os
    os.system("date")
    os.system('echo "standby 0" | cec-client -s -d 1')

  elif check == True:
    import os
    os.system("date")
    os.system('echo "on 0" | cec-client -s -d 1')

def loadpage(url):
  import os
  import webbrowser


  urltrue = url
  os.system("export DISPLAY=:0.0")
  os.system("pkill chromium & ; sleep 2")
  os.system("chromium --kiosk %s" % urltrue)
