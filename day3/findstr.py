#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __author__  = "Hexing"


#a = 'abcdefabdddd'
#b = 'h'


def findstr(a,b ):

     x = a.split(b)
     if len(a) > len(b):

         if len(x) < len(a):
             print "match"
             return 1
         else:
             print "no match"
             return -1
     else:
         print "no match"
         return -1
findstr("abcdef","assb")



