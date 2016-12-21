#!/usr/bin/env python
import os,sys
class FooClass:

    def __init__(self,name = 'Good',salary = 200):
        """

        :type name: object
        """
        self.name = name
        self.salary = salary

    def  showname(self,data):
        return self.salary+data


foo  = FooClass("xxxx")
print foo.showname(300)


foo.good = 'good'
print dir(foo)

