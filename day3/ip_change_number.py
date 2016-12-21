#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __author__  = "Hexing"

number = raw_input("please input a  12char long number:")
if len(number) == 12:
    print "your ip : %s.%s.%s.%s:"%(number[0:3],number[3:6],number[6:9],number[9:12])
else:
    print "your input no vaild"


ip = raw_input("please input a  vaild ip address:")
tmp = ip.split(".")
print "your number: %d%03d%03d%03d" %(int(tmp[0]),int(tmp[1]),int(tmp[2]),int(tmp[3]))


