#!/usr/bin/env python
import os,sys
#hexing   2016-11-30
# 3 layers lookup feature
menu  =  {'Beijing':{'Chaoyao':['chaoyao1','chaoyao2'],'Haidian':['haidian1','haidian2','haidian3'],'Feitai':['feitai1','feitai2']},'Shanghai':{'Huangpu':['huangpu1','huangpu2'],'Hongqiao':['hongqiao1','hongqiao2']}}
returnflag = False
while not returnflag:
    message1 = '''
    enter q to quit
    please chose a number:
    '''
    message2 = '''
    enter b to back
    enter q to quit
    please chose a number:
    '''
    message3 = '''
    This is a final choice
    please enter b to back or q to quit:
    '''
    level1 = menu.keys()

    for index,key in enumerate(menu.keys()):
        print '--->',index,key


    input1 = raw_input(message1).strip()
    try:
        if input1.isdigit():
            chose1 = int(input1)
            city = level1[chose1]


            while not returnflag:
                for index,key in  enumerate(menu[city]):
                    print '--->--->',index,key
                input2 = raw_input(message2).strip()
                try:

                    if input2.isdigit():
                        chose2 = int(input2)
                        area = menu[city].keys()[chose2]

                        while not returnflag:

                            for index, key in enumerate(menu[city][area]):
                                print '--->--->--->',index,key
                            try:
                                input3 = raw_input(message3).strip()

                                if input3 == "b":
                                    break
                                elif input3 == "q":
                                    returnflag = True
                            except:
                                print "enter invalid ,please follow messages do "

                    elif input2 == 'b':
                        break
                    elif input2 == 'q':
                        returnflag = True
                except:
                    print "enter invalid ,please follow messages do i2 "
        elif input1 == 'q':
            break
    except:
        print "out of index !,or enter invalid ,please follow messages do "
























