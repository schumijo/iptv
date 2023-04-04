import urlquick
import re
import os
import time as t
import schedule
from datetime import datetime
from datetime import timedelta

channels = {
        "L'Équipe live 1"    : "LequipeLive1.fr",
        "L'Équipe live 2"    : "LequipeLive2.fr",
}

def get_lives(url):
        resp = urlquick.get(url, max_age=-1)

        datas = re.compile(r'<img.+?src="(.+?)".+?>\n.+\n.+<h2.+?>\s+(.+?)\s+<\/h2>.+?<span.+?>\s+(\d+h\d?\d?)\s+<\/span>').findall(resp.text)
        if len(datas) == 0:
            return 0
        else:
            build_xmltv(datas)

def build_channels():
        print('<?xml version="1.0" encoding="UTF-8"?>')
        print('<!DOCTYPE tv SYSTEM "xmltv.dtd">"')
        print('<tv source-info-url="https://lequipe.fr" source-info-name="XML TV Lequipe Live 1-2" generator-info-name="XML TV Lequipe Live" generator-info-url="https://test.fr">')

        for key,val in channels.items():
                print('  <channel id="' + channels[key] + '">')
                print('    <display-name>' + key + '</display-name>')
                print('    <icon src=""/>')
                print('  </channel>')

def build_xmltv(datas):
        icon = datas[0][0]
        title = datas[0][1]
        hour = datas[0][2]

        hours = hour.split('h')
        if hours[1] == '':
            hours[1] = 0
        hour = "%02d%02d00" % (int(hours[0]),int(hours[1]))

        time = datetime.now()
        start_time = time.strftime('%Y%m%d') + hour

        hours = datas[1][2].split('h')
        if hours[1] == '':
            hours[1] = 0
        hour = "%02d%02d00" % (int(hours[0]),int(hours[1]))
        time = datetime.now()
        end_time = time.strftime('%Y%m%d') + hour

        print('  <programme start="' + start_time + ' +0200" stop="' + end_time + ' +0200" channel="' + channels[channel] + '">')
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
        build_channels()
        url = 'https://www.lequipe.fr/tv/videos/live/k1kypsRZF9plQhqwBRS'
        get_lives(url)
        
        url = 'https://www.lequipe.fr/tv/videos/live/k5TgcOKBUTM2KnqwBWC'
        get_lives(url)

main()
