#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __author__  = "Hexing"
import copy

d  =  {'name': 'hxing', 'sex': 'fale'}
b = {'sex':'fale'}
a = copy.deepcopy(d)
c = b.copy()
d['name'] = 'greg'
b['sex'] = 'man'
f = list(d.values())


print  "d:",d
print  "a:",a
print  "c:",c
print  "f:",f