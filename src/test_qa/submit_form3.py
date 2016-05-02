import mechanize

url = "http://q.stock.sohu.com/cn/600028/lshq.shtml"
br = mechanize.Browser()
br.set_handle_robots(False) # ignore robots
br.open(url)
br.select_form(name="historyHqForm")
br["sd"] = "2015-12-15"
br["ed"] = "2015-12-15"
br["t"][0] = "d"
res = br.submit()
content = res.read()
with open("mechanize_results.html", "w") as f:
    f.write(content)