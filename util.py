#coding=utf-8
import urllib
import sys

def real_code(code):
    if isinstance(code, int)
        code = str(code)
    if len(code) <=0 or code is None:
        return ""
    if not code.isdigit():
        return code
    code = int(code)
    if code == 100000:
        return "sz100000"
    if code > 400000:
        code = "sh" + str(code)
    else:
        code = "sz" + str(code)

def get_current_price(code)
