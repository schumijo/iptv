import urlquick
import re
import os
import time as t
import schedule
from datetime import datetime
from datetime import timedelta

channels = {
        "L'Équipe Live 2" : "LequipeLive2.fr",
        "L'Équipe Live 3" : "LequipeLive3.fr",
        "L'Équipe Live 4" : "LequipeLive4.fr",
        "L'Équipe Live 5" : "LequipeLive5.fr",
        "L'Équipe Live 6" : "LequipeLive6.fr",
        "L'Équipe Live 7" : "LequipeLive7.fr",
        "L'Équipe Live 8" : "LequipeLive8.fr",
        "L'Équipe Live 9" : "LequipeLive9.fr",
        "L'Équipe Live 10" : "LequipeLive10.fr",
        "L'Équipe Live 12" : "LequipeLive12.fr",
        "L'Équipe Live 13" : "LequipeLive13.fr",
        "L'Équipe Live 14" : "LequipeLive14.fr",
        "L'Équipe Live 15" : "LequipeLive15.fr"
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

        for data in datas:
            icon = data[0]
            channel = data[1]
            hour = data[2]
            title = data[3]

            if channel == 'la chaine L\'Équipe':
                continue

            hours = hour.split('h')
            if hours[1] == '':
                hours[1] = 0
            hour = "%02d%02d00" % (int(hours[0]),int(hours[1]))

            time = datetime.now()
            start_time = time.strftime('%Y%m%d') + hour
            time = datetime.strptime(start_time, '%Y%m%d%H%M%S') + timedelta(hours=4)
            end_time = time.strftime('%Y%m%d%H%M%S')

            print('  <programme start="' + start_time + ' +0100" stop="' + end_time + ' +0100" channel="' + channels[channel] + '">')
            print('    <title lang="fr">' + title + '</title>')
            print('    <desc lang="fr">' + title + '</desc>')
            print('    <category lang="fr">Sport</category>')
            print('    <icon src="' + icon + '"/>')
            print('    <rating system="CSA">')
            print('      <value>Tout public</value>')
            print('    </rating>')
            print('  </programme>')

        print('</tv>')


def main():
        get_lives()

main()
