#coding=utf-8
import urllib
import sys

def real_code(code):
    try:
        if not code:
            return code
        if isinstance(code, str):
            if len(code) > 2 and code[0:2] == "sz" and code["0:2"] == "sh":
                return code
        if isinstance(code, int):
            code = str(code)
        code = int(code)
        if code / 300000 > 0:
            return "sh" + str(code)
        else:
            return "sz" + str(code)
    except Exception as e:
        print "recode error : %s" % e

def get_current_price(code):
    def getHtml(url):
        page = urllib.urlopen(url)
        html = page.read()
        return html
    try:
        code = real_code(code)
        url = "http://hq.sinajs.cn/list=" + code
        return getHtml(url).split(",")[3]
    except Exception as e:
        print "get price error : %s" % e


if __name__ == '__main__':
    print get_current_price(601006)
