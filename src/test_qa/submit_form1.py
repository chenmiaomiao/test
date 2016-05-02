import requests
import webbrowser

url = "http://q.stock.sohu.com/cn/600028/lshq.shtml"
payload = {'sd':'2015-12-15','ed':'2015-12-15', 't':'d'}
r = requests.post("http://q.stock.sohu.com/cn/600028/lshq.shtml", data={'sd': '2015-07-25', 'ed': '2015-07-25', 't': 'd'})
r = requests.post(url, payload)
with open("results.html", "w") as f:
    f.write(r.content)
webbrowser.open("results.html")