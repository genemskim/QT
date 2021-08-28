import sys
import datetime
from urllib import request

if len(sys.argv) > 1:
    date = datetime.datetime.strptime(sys.argv[1], "%Y%m%d") 
    year = date.year
    day = date.__format__("%Y%m%d")
else :
    date = datetime.datetime.now()
    year = date.year
    day = date.__format__("%Y%m%d")

print(date)
print(year)
print(day)

nextDay = datetime.timedelta(days=1)

while 1 :
    url = "http://meditation.su.or.kr/meditation_mp3/%d/%s.mp3" %(year,day)
    localFile = "%s.mp3" %day
    date += nextDay
    year = date.year
    day = date.__format__("%Y%m%d")
    print(url)
    request.urlretrieve(url, localFile)
