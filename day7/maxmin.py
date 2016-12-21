#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __author__  = "Hexing"
class Test:
    def max2(self,a,b):
        self.a = a
        self.b = b
        if self.a > self.b :
            print self.a
        else:
            print self.b
    def min2(self,a,b):
        self.a = a
        self.b = b
        if self.a > self.b:
            print self.b
        else:
            print self.a
t  =  Test()
t.max2(5,99)