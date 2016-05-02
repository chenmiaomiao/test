import urllib
import urllib2
import webbrowser

url = "http://q.stock.sohu.com/hisHq"
data = urllib.urlencode({'code': 'cn_600028', 'start': '20150725', 'end': '20150725'})
print data
results = urllib2.urlopen(url, data)
with open("results.html", "w") as f:
    f.write(results.read())

webbrowser.open("results.html")