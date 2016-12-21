#!/usr/bin/evn  python
import os,sys
a = ['hell','name','goood']
for i,x in enumerate(a):
    print i,x
t = [ j * 2 for j in range(9) if j < 5 ]
print t
for  xx in t:
    print xx

f  = file('/tmp/kkk','a+')
for eachline in f:
    print eachline,

