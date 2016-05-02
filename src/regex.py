# _*_ coding: utf8 _*_

# import sys
# print sys.getdefaultencoding()  

import re
a = ">bc3↑<"
b = re.findall('>(.+?)(?:\xe2\x86\x91)*<', a)
print b

cc  = "<>a<2>a<>"
ccc = re.findall('(?!>a<)(>a<)',cc)
print ccc


html5 = """<td><div align="center">    <a href="/corp/view/vCI_StockHolderAmount.php?stockid=000004&amp;type=holdstocknum&amp;code=80002710" target="_blank">  3- a  </a><font style="color:red">↑</font></div></td>"""

cat = re.findall('(?!>(?:\s)*<|>[^<>]*\\xe2\\x86\\x91[^<>]*<|>[^<>]*\\xe2\\x86\\x93[^<>]*<)>(?:\s)*([^<>]+?)(?:\s)*<', html5)
print cat




# 
# html = """<tr class=""><td width="15%" class="head"><a name="2015-09-30"></a><div align="center"><strong>截至日期</strong></div></td><td colspan="4">2015-09-30</td></tr>"""
# html2 = """<tr class=""><td width="15%" class="head"><a name="20150930"></a><div align="center"><strong>截至日期</strong></div></td><td colspan="4">20150930</td></tr>"""
# html3 = """<td colspan="4">"22550"<a href="/corp/go.php/vCI_StockHolderAmount/code/300463/type/amount.phtml" target="_blank">查看变化趋势</a></td>"""
# html4 = """<tr class="gray">
#               <td class="head"><div align="center">5</div></td>
#               <td><div align="center"><a href="/corp/view/vCI_HoldStockState.php?stockid=300463&amp;stockholderid=30331130" target="_blank">王传英</a></div></td>
#               <td><div align="center"><a href="/corp/view/vCI_StockHolderAmount.php?stockid=300463&amp;type=holdstocknum&amp;code=30331130" target="_blank">11433400</a>&nbsp;</div></td>
#               <td><div align="center"><a href="/corp/view/vCI_StockHolderAmount.php?stockid=300463&amp;type=holdstockproportion&amp;code=30331130" target="_blank">6.15</a>&nbsp;</div></td>
#               <td><div align="center">流通A股</div></td>
#               </tr>"""
# 
# html_parse1 = re.findall('>((?=.*?-)(?=.*?\d))<', html)
# html_parse2 = re.findall('>([\d-]*(?:-)[\d-]*)<', html)
# html_parse3 = re.findall('>\D*?(\d+)\D*?<', html3)
# html_parse4 = re.findall('>([^<>\n]+?)<', html4.decode('unicode-escape').encode('utf-8'))
# 
# print html_parse1
# print html_parse2
# print html_parse3
# print str(html_parse4).decode('utf-8')

# def testreturn():
#     
#     print 1
#     return 0
# 
# print testreturn()