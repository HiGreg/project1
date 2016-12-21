#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# __author__  = "Hexing"
goods = [['apple',20000],['tv',450],['car',43000],['banna',400]]
buylist = {}
#define customer account of goods
goodsaccount = {}
salary = int(raw_input("please enter your salary:").strip())
buys_list = []
i = 1
while True:

    for index,line in enumerate(goods):
        print index,line[0],line[1]
    choose = raw_input("please  select  goods number or enter q to quit:")
    if choose.isdigit():
        buys = int(choose)

        try:
            prices = goods[buys]
            if prices[1] < salary:
                #buys_list.append("%s %d" %(prices[0],prices[1]))
                if  prices[0] not in buylist.keys():

                    buylist[prices[0]] = prices[1]

                    goodsaccount[prices[0]] = 1
                    salary  -= prices[1]
                    print '''You had bought list of goods :
goods  total'''
                    for good in buylist:
                        print good,buylist[good]
                    for good in goodsaccount:
                        print "------\n"
                        print '''You had bought :
goods  account'''
                        print good,goodsaccount[good],"\n"
                else:
                    buylist[prices[0]] += prices[1]
                    i += 1
                    goodsaccount[prices[0]] = i
                    print '''You had bought list of goods:
goods  total'''
                    for good in buylist:
                        print good,buylist[good]
                    for good in goodsaccount:
                        print "------\n"
                        print '''You had bought :
goods  account'''
                        print good, goodsaccount[good],'\n'
            else:
                print "your balance is not enough"
        except IndexError:
            print "you input number out of index,please check it!"

    elif choose == 'q':
        print '''You had bought list of goods:
        goods  total'''
        for good in buylist:
            print good, buylist[good]
        for good in goodsaccount:
            print "------\n"
            print '''You had bought :
        goods  account'''
            print good, goodsaccount[good],"\n"
        print "your account balance :%d" %salary
        break
