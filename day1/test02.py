#/usr/bin/env python
import copy
a = ['helloman',['sex'],100]
b = a[:]
c = b
d = copy.deepcopy(a)
print d
print a,b
print [id(x) for x in a,b,c,d]
a[1][0] = 'good'
b[1][0]= "bad"
print "-----------" ,a ,b ,c,d
import copy



