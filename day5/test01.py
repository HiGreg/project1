#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __author__  = "Hexing"

a  = {'name':'jiajia','age':23,'sex':'female'}
defaulterror = "your input the number no valid "
def longestlineinfile(path):
    f = open(path,'r')
    #lines  = f.readlines()
    #f.close()
    longest  = 0
    for line in f:
        print line 
    #     linelen = len(line.split())
    #     if linelen > longest:
    #         longest  = linelen
    # return  longest
print  longestlineinfile("/var/log/messages")





