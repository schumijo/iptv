#!/bin/bash

python3 parser/lequipe.py k1kypsRZF9plQhqwBRS http://51.83.116.6:22754 > playlists/lequipe/lequipelive1.m3u8
python3 parser/lequipe.py k5TgcOKBUTM2KnqwBWC http://51.83.116.6:22754 > playlists/lequipe/lequipelive2.m3u8
python3 parser/lequipe.py kXRfcKHV9HhcZuqwBYP http://51.83.116.6:22754 > playlists/lequipe/lequipelive3.m3u8

exit 0
