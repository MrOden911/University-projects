from math import *

def fun(x,f):
    try:
        if type(f)!=str:
            return eval(str(f))
        else:
            return eval(f)
    except Exception:
        return ''
