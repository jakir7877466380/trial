#!/usr/bin/python
# -*- coding: UTF-8 -*-

from os import system, name
import itertools
import threading
import time
import sys
import datetime
from base64 import b64decode,b64encode
from datetime import date

expirydate = datetime.date(2021, 9, 24)
#expirydate = datetime.date(2021, 8, 30)
today=date.today()
def hero():

    def chalo():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']) :
                if done:
                    break
                sys.stdout.write('\rhacking in the parity server for next colour--------- ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rDone!     ')

        t = threading.Thread(target=animate)
        t.start()

        #long process here
        time.sleep(20)
        done = True

    def chalo1():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rgetting the colour wait --------- ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rDone!     ')

        t = threading.Thread(target=animate)
        t.start()

        #long process here
        time.sleep(20)
        done = True

    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
    def getSum(n):
        sum=0
        for digit in str(n):
            sum+= int(digit)
        return sum
    def lawde_time_pe_khel(n):
        check=0
        for digit in (n):
            if(int(digit)==0):
                check=check+1
        return check
    clear()
    y=1
    newperiod=period
    banner='figlet RXCE'
    numbers=[]
    while(y):
        clear()
        system(banner)
        print("Contact me on telegram @smsn_knt")
        print("Enter ",newperiod," Parity Price :")
        current=input()
        current=int(current)
        chalo()
        print("\n---------Successfully hacked the server-----------")
        chalo1()
        print("\n---------Successfully got the colour -------------")
        print('\n')
        last2=str(current)[-2:]
        samjha_maadarchod=lawde_time_pe_khel(last2)
        if(newperiod%2==0):
            sum=getSum(current)
            if(sum%2==0):
                print(newperiod+1," : 🔴, RED")
            else:
                print(newperiod+1,"  : 🟢, GREEN")
        else:
            sum=getSum(current)
            if(sum%2==0):
                print(newperiod+1,"   : 🔴, RED")
            else:
                print(newperiod+1,"   : 🟢, GREEN")
        newperiod+=1
        numbers.append(current)
        y=input("Do you want to play : Press 1 and 0 to exit \n")
        if(y==0):
            y=False
        if (len(numbers)>11):
            clear()
            system('figlet Thank you!!')
            print("Play on next specified time!!")
            print("-----------Current Time UP----------")
            sys.exit(" \n \n \n Contact on Telegram @smsn_knt")
            #print(numbers)
  



if(expirydate>today):
    now = datetime.datetime.now()
    First = now.replace(hour=13, minute=55, second=0, microsecond=0)
    Firstend = now.replace(hour=14, minute=35, second=0, microsecond=0)
    Second = now.replace(hour=16, minute=25, second=0, microsecond=0)
    Secondend = now.replace(hour=17, minute=35, second=0, microsecond=0)
    Third = now.replace(hour=15, minute=55, second=0, microsecond=0)
    Thirdend = now.replace(hour=16, minute=35, second=0, microsecond=0)
    Final = now.replace(hour=17, minute=55, second=0, microsecond=0)
    Finalend = now.replace(hour=18, minute=35, second=0, microsecond=0)

    if (now>Third and now<Thirdend):
            period=320
            hero()
    elif(False):
            period=340
            hero()
    elif(False):
            period=340
            hero()
    elif(False):
            period=360
            hero()
    else:
        banner='figlet RXCE'
        system(banner)
        #print("Hi!! Thanks for buying the hack")
        print("Hi! thanks for trying our DEMO")
        print("----------Your play time-----------")
        #print("31st Aug 2021, 11:00 AM- 11:30 AM")
        #print("31st Aug 2021, 02:00 PM- 02:30 PM")
        print("23rd Sept 2021, 04:00 PM- 04:30 PM")
        #print("31st Aug 2021, 08:00 PM- 08:30 PM")
        print("Please play on the given time, and ")
        print("If you think it is an error contact")
        print(" admin on telegram @smsn_knt ")



else:
    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
    code="MRLEOPARD"
    test="MASTRAM"
    #nextday="NITESH9013"
    banner='figlet RXCE'
    system(banner)
    print("*---------*----------*-------------*----------*")
    print("Your hack has expired--- Please contact")
    print(" on telegram ----@smsn_knt for activating")
    print(" Recharge Amount :        Total limit " )
    print(" 1.     1000 INR -------  1 Day (30 Games")
    print(" 2.     5000 INR -------  7 Days(210 Games")
    print("*---------*----------*-------------*----------*")
    print("Your custom hack can be made request from us.")
    print("Beware of fraudsters!!!")
    while(True):
        print("My banking name is SUNNY KUMAR")
        print("If you send to any other name , then IT IS SCAMMM")
        print("--------*--------*----------*---------")
        print("send payment only to SUNNY KUMAR ")
        print("payhere--- UPI : ")
        print("UPI1 : mdurth@ybl")
        print("UPI2 : sunnyk16@fbl")
        print("If you have already paid to above UPI")
        print("Please Enter your 12 Digit \n UPI reference number ")
        print("or please Enter Correct activation code for 8:30 PM ")
        bhai=input(": ")
        if(bhai==code or bhai==test):
            clear()
            print("----------Your play time-----------")
            print("25th Nov 2021, 02:30 PM- 03:00 PM")
            print("25th Nov 2021, 05:00 PM- 05:30 PM")
            print("25th Nov 2021, 08:30 PM- 09:00 PM")
            print("Please play on the given time, and ")
            print("If you think it is an error contact")
            print("wait.... starting....")
            time.sleep(20)
            period=290
            hero()
            #print("Today Server is off because I am out ")
            #rint(" of town, Tomorrow It will work as usual.")
            #print(" Thank You!!")
            #rint("To all the weekly members next week, cost will be  ")
            #print(" 4000 INR , because in this week 2 days off " )
            #print("Thank You!! ")
            sys.exit(" \n \n \n Contact on Telegram @smsn_knt")
        elif(bhai==nextday or bhai==nexday1):
            clear()
            banner='figlet RXCE'
            system(banner)
            print("----------Your play time-----------")
            #print("8th-14th Nov 2021, 02:30 PM- 03:00 PM")
            #print("8th-14th Nov 2021, 06:00 PM- 06:30 PM")
            #print("8th-14th Nov 2021, 08:30 PM- 09:00 PM")
            #print("Please play on the given time, and ")
            #print("If you think it is an error contact")
            #print("wait.... starting....")
            time.sleep(20)
            period=290
            hero()
            period("Sorry too many people(>20) using hack in same time ")
            sys.exit(" \n \n \n Contact on Telegram @smsn_knt")
            
            
        else:
            clear()
            banner='figlet RXCE'
            system(banner)
            print("Incorrect Activation Code :")
     
