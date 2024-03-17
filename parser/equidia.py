#! /usr/bin/python3
# Thanks to pshanmu3 user on github
import requests
import os
import sys

proxies = {}
if len(sys.argv) == 3:
    proxies = {
                'http' : sys.argv[2],
                'https' : sys.argv[2]
              }

na = 'https://raw.githubusercontent.com/naveenland4/UTLive/main/assets/info.m3u8'
def grab(id):
    headers={
        "User-Agent": "Equidia/6036 CFNetwork/1220.1 Darwin/20.3.0",
        "Referer": "https://fr.equidia.app/"
    }
    try:
        playlist = s.get('https://api.equidia.fr/api/public/racing/equidia-mobileapp-ios-1/equidia-'+id, headers=headers, proxies=proxies).json()['primary']
    except Exception as e:
        playlist = na

    try:
        m3u = s.get(playlist, proxies=proxies)
    except Exception as e:
        m3u = na
    finally:
        print(m3u.text.replace("slot", playlist.replace("playlist.m3u8","") + "/slot"))

s = requests.Session()

if (sys.argv[1] == 'equidia'):
    id = 'live2'
elif (sys.argv[1] == 'trot'):
    id = 'racingtrot'
elif (sys.argv[1] == 'galop'):
    id = 'racinggalop'
elif (sys.argv[1] == 'mag'):
    id = 'racingmag'
elif (sys.argv[1] == 'racing1'):
    id = 'racing1'
elif (sys.argv[1] == 'racing2'):
    id = 'racing2'
elif (sys.argv[1] == 'racing3'):
    id = 'racing3'
elif (sys.argv[1] == 'racing4'):
    id = 'racing4'
elif (sys.argv[1] == 'racing5'):
    id = 'racing5'
else:
    sys.exit(1)

grab(id)
