#!/bin/bash

cat playlists/iptv/fr.m3u8 > fr.m3u8
tail -n +2 playlists/iptv/fr_mytf1_fast.m3u8 >> fr.m3u8
wget https://i.mjh.nz/SamsungTVPlus/fr.m3u8 -O - >> fr.m3u8

exit 0
