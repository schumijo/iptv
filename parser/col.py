#! /usr/bin/python3
import requests
import os
import sys

na = 'https://github.com/BG47510/Zap/raw/main/assets/error.m3u8'
def grab(url):
    headers={
        "Referer": "http://callofliberty.fr/",
        "Origin": "http://callofliberty.fr",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }
    try:
        m3u = s.get(url, headers=headers)
    except Exception as e:
        m3u = na
    finally:
        print(m3u.text)
 
s = requests.Session()

grab(sys.argv[1])
