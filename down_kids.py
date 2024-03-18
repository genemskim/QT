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
    url = "https://sum.su.or.kr:8888/Bible_Attach/QT3/G%s-1.jpg" %day
    localFile = "%s-1.jpg" %day
    print(url)
    request.urlretrieve(url, localFile)

    url = "https://sum.su.or.kr:8888/Bible_Attach/QT3/G%s-2.jpg" %day
    localFile = "%s-2.jpg" %day
    print(url)
    request.urlretrieve(url, localFile)

    date += nextDay
    year = date.year
    day = date.__format__("%Y%m%d")