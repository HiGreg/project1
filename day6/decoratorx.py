#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __author__  = "Hexing"
from functools import wraps
def login(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        vaild = raw_input('please input a login name:')
        if vaild == 'greg':
            print '======welcome to  Greg '
            return  func(*args,**kwargs)
    return wrapper

def test1():
    print "test001"
@login
def test2(name):
    print "test02sssssss"

    return name


x = test2("xxx")

print x.__class__
print  x