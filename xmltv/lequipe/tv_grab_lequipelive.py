import urlquick
import re
import os
import time as t
import schedule
from datetime import datetime
from datetime import timedelta

channels = {
        "L'Équipe live 3"    : "LequipeLive3.fr",
        "L'Équipe live 4"    : "LequipeLive4.fr",
        "L'Équipe live 5"    : "LequipeLive5.fr",
        "L'Équipe live 6"    : "LequipeLive6.fr",
        "L'Équipe live 7"    : "LequipeLive7.fr",
        "Journal du Golf TV" : "JournalduGolfTV.fr"
}

def get_lives():
        resp = urlquick.get("https://www.lequipe.fr/directs", max_age=-1)

        datas = re.compile(r'<article.+?<img.+?src="(.+?)".+?alt="(.+?)".+?<span class="ColeaderWidget__scheduledEvent".+?>\s+(\d+h\d?\d?)(?:\n.+?)+<p class="ColeaderWidget__subtitle".+?>(.+?)<\/p>').findall(resp.text)
        if len(datas) == 0:
            return 0
        else:
            build_xmltv(datas)

def build_xmltv(datas):
        print('<?xml version="1.0" encoding="UTF-8"?>')
        print('<!DOCTYPE tv SYSTEM "xmltv.dtd">"')
        print('<tv source-info-url="https://test.fr" source-info-name="XML TV Lequipe Live" generator-info-name="XML TV Lequipe Live" generator-info-url="https://test.fr">')

        for key,val in channels.items():
                print('  <channel id="' + channels[key] + '">')
                print('    <display-name>' + key + '</display-name>')
                print('    <icon src=""/>')
                print('  </channel>')

        i = 0
        for data in datas:
            icon = data[0]
            channel = data[1]
            hour = data[2]
            title = data[3]

            if channel == 'la chaine L\'Équipe':
                continue

            if channel == 'L\'Équipe live 1':
                continue

            if channel == 'L\'Équipe live 2':
                continue

            hours = hour.split('h')
            if hours[1] == '':
                hours[1] = 0
            hour = "%02d%02d00" % (int(hours[0]),int(hours[1]))

            time = datetime.now()
            start_time = time.strftime('%Y%m%d') + hour
            time = datetime.strptime(start_time, '%Y%m%d%H%M%S') + timedelta(hours=4)
            end_time = time.strftime('%Y%m%d%H%M%S')

            x = i+1
            while x < len(datas):
                if datas[x][1] == channel:
                    hours = datas[x][2].split('h')
                    if hours[1] == '':
                        hours[1] = 0
                    hour = "%02d%02d00" % (int(hours[0]),int(hours[1]))
                    time = datetime.now()
                    end_time = time.strftime('%Y%m%d') + hour
                    break
                x = x+1

            print('  <programme start="' + start_time + ' +0200" stop="' + end_time + ' +0200" channel="' + channels[channel] + '">')
            print('    <title lang="fr">' + title + '</title>')
            print('    <desc lang="fr">' + title + '</desc>')
            print('    <category lang="fr">Sport</category>')
            print('    <icon src="' + icon + '"/>')
            print('    <rating system="CSA">')
            print('      <value>Tout public</value>')
            print('    </rating>')
            print('  </programme>')

            i = i+1
        print('</tv>')


def main():
        get_lives()

main()
