import urlquick
import re
import os
from datetime import datetime
from datetime import timedelta

time = datetime.now() - timedelta(minutes=10)
start_time = time.strftime('%Y%m%d%H%M%S')
time = datetime.now() + timedelta(hours=1)
end_time = time.strftime('%Y%m%d%H%M%S')

#Channel list
channels_id = {
        "k1ZUdcthDLhoYjgMfdf" : "LequipeLive2.fr",
        "k1kypsRZF9plQhqwBRS" : "LequipeLive3.fr",
        "k5TgcOKBUTM2KnqwBWC" : "LequipeLive4.fr",
        "kXRfcKHV9HhcZuqwBYP" : "LequipeLive5.fr",
        "k6oih7JyuEmhrnqwBZT" : "LequipeLive6.fr",
        "k3HiS3JB0BsORKqwC49" : "LequipeLive7.fr",
        "k6P3xLH5tTtGSgqwC4P" : "LequipeLive8.fr",
        "k1y3Q3GC7w8flQry8S3" : "LequipeLive9.fr",
        "k5VKYQn5hAE4vfry927" : "LequipeLive10.fr",
        "k2Z9T8IhyLWvyPtITYJ" : "LequipeLive12.fr",
        "k53cYSxIs49Vf0wkv86" : "LequipeLive13.fr",
        "k7rZDp22dyZ25EwkvsF" : "LequipeLive14.fr",
        "k6c3A07yUljlAzwkvtL" : "LequipeLive15.fr"
}

channels_name = {
        "k1ZUdcthDLhoYjgMfdf" : "L\'Equipe Live 2",
        "k1kypsRZF9plQhqwBRS" : "L\'Equipe Live 3",
        "k5TgcOKBUTM2KnqwBWC" : "L\'Equipe Live 4",
        "kXRfcKHV9HhcZuqwBYP" : "L\'Equipe Live 5",
        "k6oih7JyuEmhrnqwBZT" : "L\'Equipe Live 6",
        "k3HiS3JB0BsORKqwC49" : "L\'Equipe Live 7",
        "k6P3xLH5tTtGSgqwC4P" : "L\'Equipe Live 8",
        "k1y3Q3GC7w8flQry8S3" : "L\'Equipe Live 9",
        "k5VKYQn5hAE4vfry927" : "L\'Equipe Live 10",
        "k2Z9T8IhyLWvyPtITYJ" : "L\'Equipe Live 12",
        "k53cYSxIs49Vf0wkv86" : "L\'Equipe Live 13",
        "k7rZDp22dyZ25EwkvsF" : "L\'Equipe Live 14",
        "k6c3A07yUljlAzwkvtL" : "L\'Equipe Live 15"
}

# Read db file
prog = {}
if os.path.getsize('/usr/bin/xml_lequipe.db') > 1:
  f = open("/usr/bin/xml_lequipe.db", "r")
  for line in f:
    key, value = line.split(";")
    prog[key] = value.replace("\n","")
  f.close()

print('<?xml version="1.0" encoding="UTF-8"?>')
print('<!DOCTYPE tv SYSTEM "xmltv.dtd">"')
print('<tv source-info-url="https://test.fr" source-info-name="XML TV Lequipe Live" generator-info-name="XML TV Lequipe Live" generator-info-url="https://test.fr">')

for key,val in channels_id.items():
  print('  <channel id="' + channels_id[key] + '">')
  print('    <display-name>' + channels_name[key] + '</display-name>')
  print('    <icon src=""/>')
  print('  </channel>')

resp = urlquick.get("https://www.lequipe.fr/directs", max_age=-1)
live_id = re.compile(r'<article.+?<a href="(.+?)".+?src="(.+?)".+?alt="(.+?)"').findall(resp.text)
for a in live_id:
  link = a[0]
  icon = a[1]
  title = a[2]
  link_id = link.split("/")[-1]
  if link_id == "k5s40USR9HxnG5aCf1y":
    continue
  channel = channels_id[link_id]

  if title in prog:
    time = datetime.now()
    start_time = time.strftime('%Y%m%d') + prog[title].replace('h','') + '00 +0200'

  print('  <programme start="' + start_time + ' +0200" stop="' + end_time + ' +0200" channel="' + channel + '">')
  print('    <title lang="fr">' + title + '</title>')
  print('    <desc lang="fr">' + title + '</desc>')
  print('    <category lang="fr">Sport</category>')
  print('    <icon src="' + icon + '"/>')
  print('    <rating system="CSA">')
  print('      <value>Tout public</value>')
  print('    </rating>')
  print('  </programme>')

print('</tv>')

live_id = re.compile(r'<article.+?<img.+?alt="(.+?)".+?<span class="ColeaderWidget__scheduledEvent".+?>\s+((\d+h\d+)|(\d+h))\s+').findall(resp.text)
f = open("/usr/bin/xml_lequipe.db", "a")
for a in live_id:
  if a[0] not in prog:
    heure=a[1].split('h')
    if heure[1] == '':
      heure[1]=0
    f.write("{0};{1:02d}h{2:02d}\n".format(a[0],int(heure[0]),int(heure[1])))
f.close()
