#!/usr/bin/env  python
import os,sys

l = [1,'hell','helldh','jiace']
f = ['hell','jacek']

try:

    print l[::3]
except IndexError:
    print "index out of  range !!,index must in :",len(l)
else:
    print  "good job"

a = 'abcdefg'
for i in [None] + range(-1,-len(a),-1):
    print a[:i]


import  string
print a.upper()
print a.lower()
print string.uppercase
print string.letters
print string.digits,; print string.lowercase