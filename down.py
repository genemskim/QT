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

while True :
    try :
        url = "http://meditation.su.or.kr/meditation_mp3/%d/%s.mp3" %(year,day)
        localFile = "%s.mp3" %day
        print(url)
        request.urlretrieve(url, localFile)
    except Exception as e :
        print("Error: %s" %e)
        break
    date += nextDay
    year = date.year
    day = date.__format__("%Y%m%d")
