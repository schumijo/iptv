#!/bin/bash

python3 parser/col.py http://s2.callofliberty.fr/direct1/TF1/master.m3u8 > playlists/col/tf1.m3u8
python3 parser/col.py http://s2.callofliberty.fr/direct1/W9/index.m3u8  > playlists/col/w9.m3u8
python3 parser/col.py http://s2.callofliberty.fr/direct1/TFX/master.m3u8 > playlists/col/tfx.m3u8
python3 parser/col.py http://s2.callofliberty.fr/direct1/TF1SERIESFILMS/master.m3u8 > playlists/col/tf1sf.m3u8
python3 parser/col.py http://s2.callofliberty.fr/direct1/6ter/index.m3u8 > playlists/col/6ter.m3u8
python3 parser/col.py http://s2.callofliberty.fr/direct1/NRJ12/index.m3u8 > playlists/col/nrj12.m3u8
python3 parser/col.py http://s2.callofliberty.fr/direct1/Cherie25/index.m3u8 > playlists/col/cherie25.m3u8

exit 0
