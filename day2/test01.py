#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __author__  = "Hexing"
import fileinput
for line in fileinput.input('test.txt',inplace = 1):
    print line.replace('LINE','Lx'),


