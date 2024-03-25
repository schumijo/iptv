#!/bin/bash

python3 parser/col.py http://s2.callofliberty.fr/directlive/TF1/master.m3u8 > playlists/col/tf1.m3u8
python3 parser/col.py http://s2.callofliberty.fr/directlive/W9/master.m3u8  > playlists/col/w9.m3u8
python3 parser/col.py http://s2.callofliberty.fr/directlive/TFX/master.m3u8 > playlists/col/tfx.m3u8
python3 parser/col.py http://s2.callofliberty.fr/directlive/TF1SERIESFILMS/master.m3u8 > playlists/col/tf1sf.m3u8
python3 parser/col.py http://s2.callofliberty.fr/directlive/6ter/master.m3u8 > playlists/col/6ter.m3u8
python3 parser/col.py http://s2.callofliberty.fr/directlive/NRJ12/index.m3u8 > playlists/col/nrj12.m3u8
python3 parser/col.py http://s2.callofliberty.fr/directlive/Cherie25/index.m3u8 > playlists/col/cherie25.m3u8

exit 0
