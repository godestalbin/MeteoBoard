#Meteo widget

import urllib.request
content = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/forecast?id=6454427&mode=xml&APPID=8bb4878f2fd5be4923cf4da047064f72").read()

print(content)