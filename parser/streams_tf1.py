import urlquick
import re
import os
import unidecode

resp = urlquick.get("https://www.tf1.fr/stream", max_age=-1)
datas = re.compile(r'<div class="ScheduleItem_container_ZB9rN"><a.+?.+?href="(.+?)"(.+?\n)+?.+?<img src="(.+?)".+?alt="Logo (.+?)"').findall(resp.text)

print('#EXTM3U')

i=1
for data in datas:
        tvid = unidecode.unidecode(data[3])
        tvid = re.sub(r'[^a-zA-Z0-9]', '', tvid)
        print ('#EXTINF:-1 tvg-id="TF1' + tvid + '.fr" tvg-chno="' + str(i) + '" tvg-logo="' + data[2] +'",'+ data[3])
        print ('pipe:///usr/local/bin/streamlink --stdout --default-stream best --url https://www.tf1.fr' + data[0])
        i+=1
