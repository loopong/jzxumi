#coding=utf-8
import urllib
import sys

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

whine = (
        {"name":"sa", "code":"sh600703", "bought":0, "num":0},
        {"name":"kd", "code":"sh600986", "bought":0, "num":0},
        {"name":"jt", "code":"sz002176", "bought":0, "num":0},
        {"name":"lx", "code":"sz000830", "bought":0, "num":0},
        {"name":"dh", "code":"sz002236", "bought":0, "num":0},
        {"name":"ds", "code":"sz002384", "bought":0, "num":0},
        {"name":"cy", "code":"sh600525", "bought":0, "num":0},
        {"name":"wh", "code":"sh600309", "bought":0, "num":0},
        {"name":"zy", "code":"sh600216", "bought":0, "num":0},
        {"name":"bd", "code":"sh600598", "bought":0, "num":0},
        {"name":"js", "code":"sz002462", "bought":0, "num":0},
        {"name":"jd", "code":"sz300316", "bought":0, "num":0},
        {"name":"ws", "code":"sz300017", "bought":0, "num":0},
        {"name":"jc", "code":"sh600566", "bought":0, "num":0},
        {"name":"gs", "code":"sh601398", "bought":0, "num":0},
        {"name":"sz", "code":"sh000001", "bought":0, "num":0},
        {"name":"sc", "code":"sz399001", "bought":0, "num":0},
        {"name":"cy", "code":"sz399006", "bought":0, "num":0},
#        {"name":"亨通", "code":"sh600487", "bought":0, "num":0},
#        {"name":"紫鑫", "code":"sz002118", "bought":0, "num":100},
#        {"name":"大秦", "code":"sh601006"},
#        {"name":"柳工", "code":"sz000528"},
#        {"name":"天原", "code":"sz002386"},
#        {"name":"水晶", "code":"sz002273"},
        )
todayearn = 0.0
left = 742214
i = 703000
total = 0.0

for s in whine:
    name = s["name"]
    blocks = s["num"]
    bought = s['bought']
    url = "http://hq.sinajs.cn/list=" + s["code"]
    res = getHtml(url).split(",")

    price = float (res[3])
    start = float (res[2])
    delta = 0
    if bought is not 0:
        delta = (price - bought)/bought*100
    earn = ((price-start)*blocks)
    value = (price * blocks)/10000.0
    total += price*blocks
    todayearn += earn
    intval = (price - start)*100.0/start
    print "%s\t%.2f\t%.2f\t%.2f\t%.2f%%\t%d" % (name, value, delta, price, intval, earn)
#    print "%.2f\t%.2f%%" % (price, intval)
total_m = total+left
c = total/(total+left)*100
print "todayearn %d" % (todayearn)
print "totalenarn %d percent %.2f" % (total+left-i , (total+left-i)/(total+left)*100)
print "total %d" % (total+left)
print "cangwei %.2f"% c
