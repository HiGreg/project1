#!/usr/bin/env  python
import os
import sys
import string
alphas = string.letters
nums = string.digits

print 'welcome to the identifier character v.10'
print 'testees must be at least 2 chars long'

myInput = raw_input('identified to test ?:')
charlen = len(myInput)
if charlen > 1:
    if myInput[0] not in alphas:
        print ''' invalid : first symbol must be
                alphabetic'''
    else:
        myalphas = alphas + nums
        for otherChar in myInput[1:]:
            if otherChar not in myalphas:
                print '''  invalid : remaining symbols must be  alphabetic and number'''
                break
        else:
            print "good job"
else:
    print "please input  2 chars longs"