#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __author__  = "Hexing"
from functools import wraps

def Before(*args,**kwargs):
    print ("login sucessfully")
def After(*args,**kwargs):
    print("this is After")
def Findd():
    print ("this is final step")
#define decorator with pamar (before, after,findd)
def DC(*args,**kwargs):
    #define array to store func
    func_array = args
    def outer(main_func):
        @wraps(main_func)
        def wrapper(*args,**kwargs):
            func_array[0](*args,**kwargs)
            main_func(*args,**kwargs)
            func_array[1](*args,**kwargs)
            func_array[2]()
        return wrapper
    return outer

@DC(Before,After,Findd)
def Hello(name,age):
    print (" %s said hello,age is %s" % (name,age) )
Hello("Greg","20")
