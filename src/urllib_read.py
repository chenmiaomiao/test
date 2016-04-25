import urllib

url = "http://q.stock.sohu.com/hisHq?code=cn_600028&start=20150918&end=20160115&stat=1&order=D&period=d&callback=historySearchHandler&rt=jsonp&r=0.5620633495524285&0.07780711725972944"
url_open = urllib.urlopen(url)
url_read = url_open.read()
print url_read