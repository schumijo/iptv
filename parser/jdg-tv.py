#! /usr/bin/python3
import requests
import os
import sys

na = 'https://raw.githubusercontent.com/naveenland4/UTLive/main/assets/info.m3u8'
def grab():
    try:
        m3u = s.get('https://www.dailymotion.com/player/metadata/video/k5VKYQn5hAE4vfry927?embedder=https%3A%2F%2Fwww.journaldugolf.fr').json()['qualities']['auto'][0]['url']
    except Exception as e:
        m3u = na
        print(na)
        sys.exit(1)

    try:
        m3u = s.get(m3u)
    except Exception as e:
        m3u = na
    finally:
        print(m3u.text)

s = requests.Session()

grab()
