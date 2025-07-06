#!/bin/bash

cat playlists/iptv/fr.m3u8 > fr.m3u8
tail -n +2 playlists/iptv/fr_mytf1_fast.m3u8 >> fr.m3u8
iconv -f ISO-8859-1 -t UTF-8 playlists/iptv/fr_samsungtv.m3u8 > playlists/iptv/fr_samsungtv_corrected.m3u8
tail -n +2 playlists/iptv/fr_samsungtv_corrected.m3u8 >> fr.m3u8

exit 0
