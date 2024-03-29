#!/bin/bash

python3 parser/equidia.py equidia > playlists/equidia/equidia-live.m3u8
python3 parser/equidia.py trot > playlists/equidia/equidia-racingtrot.m3u8
python3 parser/equidia.py galop > playlists/equidia/equidia-racinggalop.m3u8
python3 parser/equidia.py mag > playlists/equidia/equidia-racingmag.m3u8
python3 parser/equidia.py racing1 > playlists/equidia/equidia-racing1.m3u8
python3 parser/equidia.py racing2 > playlists/equidia/equidia-racing2.m3u8
python3 parser/equidia.py racing3 > playlists/equidia/equidia-racing3.m3u8
python3 parser/equidia.py racing4 > playlists/equidia/equidia-racing4.m3u8
python3 parser/equidia.py racing5 > playlists/equidia/equidia-racing5.m3u8

exit 0
