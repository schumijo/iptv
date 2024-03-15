#! /usr/bin/python3
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
    try:
        m3u = s.get('https://www.dailymotion.com/player/metadata/video/' + id + '?embedder=https%3A%2F%2Fwww.lequipe.fr%2Ftv%2Fvideos%2Flive%2F'+ id, proxies=proxies).json()['qualities']['auto'][0]['url']
    except Exception as e:
        m3u = na
        print(na)
        sys.exit(1)

    try:
        m3u = s.get(m3u, proxies=proxies)
    except Exception as e:
        m3u = na
    finally:
        print(m3u.text)

s = requests.Session()
id = sys.argv[1]
grab(id)
