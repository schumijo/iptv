
#! /usr/bin/python3
import requests
import os
import sys

proxies = {}
if len(sys.argv) == 2:
    proxies = {
                'http' : sys.argv[1],
                'https' : sys.argv[1]
              }

na = 'https://raw.githubusercontent.com/naveenland4/UTLive/main/assets/info.m3u8'
def grab():
    try:
        m3u = s.get('https://www.dailymotion.com/player/metadata/video/k5VKYQn5hAE4vfry927?embedder=https://www.journaldugolf.fr', proxies=proxies)
    except Exception as e:
        m3u = na
        print(na)
        sys.exit(1)
    print('ok')
    print(m3u)
    try:
        m3u = s.get(m3u)
    except Exception as e:
        m3u = na
    finally:
        print(m3u.text)

s = requests.Session()

grab()
