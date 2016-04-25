import urllib2

def gen_headers(host, referer):
    header = {}
    
    header['Host'] = host
    header['Connection'] = 'keep-alive'
    header['Cache-Control'] = 'max-age=0'
    header['Accept'] = 'text/html, */*; q=0.01'
    header['X-Requested-With'] = 'XMLHttpRequest'
    header['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'
    header['DNT'] = '1'
    header['Referer'] = referer
    header['Accept-Encoding'] = 'gzip, deflate, sdch'
    header['Accept-Language'] = 'zh-CN,zh;q=0.8,ja;q=0.6'

    return header

host = 'q.stock.sohu.com'
referer = 'http://q.stock.sohu.com/cn/000002/index.shtml'
header = gen_headers(host, referer)

txheaders = {   
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Accept-Language': 'en-us',
    'Accept-Encoding': 'gzip, deflate, compress;q=0.9',
    'Keep-Alive': '300',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
}

headers = {
    'Host':'q.stock.sohu.com',
    'Connection':'keep-alive',
    'Cache-Control':'max-age=0',
    'Accept': 'text/html, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',
    'DNT':'1',
    'Referer': 'http://q.stock.sohu.com/hisHq',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6'
    }

req = urllib2.Request('http://q.stock.sohu.com/hisHq?code=cn_600028&start=20150918&end=20160115&stat=1&order=D&period=d&callback=historySearchHandler&rt=jsonp&r=0.5620633495524285&0.07780711725972944', None, headers)
respnse = urllib2.urlopen(req, timeout = 10)
html = respnse.read()
print html
