from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import random
import sys
import os
import pyttsx3


logo = """


 _,   _                 ___                          
( |  /    o            ( /          _/_      /    _/_
  | /__, ,  _ _ _       / _ _   (   /  __,  /  __ /  
  |/(_/(_(_/ / / /_---_/_/ / /_/_)_(__(_/(_/_)(_)(__ 
                                                     
                                                     
    [✔]  https://github.com/Maih4ckerHu    [✔]
    [✔]             Mr.H4cker                [✔]
    [✔]  Please Don't Use For illegal Activity  [✔]

        """                                                          

# Akele hi kafi hu 
#😈😈😈😈😈😈😈😈😈 >>>>>>>>>
#let's start >>>>>>>>>>>>>>>>>>>>>>>>
#Chalo Mr.H4cker ke sath ... Insta sms  karte hai >>>>>>>
engine = pyttsx3.init()
engine.setProperty('rate', 190)
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)
engine.say("Your bot ready for messaging")
engine.runAndWait()

print(logo)
time.sleep(1)
#prameter's
list = []
engine.say("Enter your username")
engine.runAndWait()
usrname = str(input("Enter your username : "))
engine.say("Enter your password")
engine.runAndWait()
passwd = str(input("Enter your password : "))
engine.say("Enter name of enemy username")
engine.runAndWait()
vicitmname = str(input("Enter name of vicitm : "))
engine.say("Enter threads")
engine.runAndWait()
num = int(input("Enter threads : "))

for i in range(0, num):
    engine.say("Enter message")
    engine.runAndWait()
    ourmsg = str(input("   \t Enter msg : "))
    list.append(ourmsg)

if usrname == vicitmname:
    engine.say("Your username and vicitmname are same therefore its doesn't exist try again")
    engine.runAndWait()
    time.sleep(2)
    sys.exit("------------------------WRONG-ARGUMENT------------------------")

print("\n")
engine.say("COLLECTING INFORMATION SUCCESSFULLY      and Now open browser")
engine.runAndWait()
print("-------------------COLLECTING-INFORMATION-SUCCESSFULLY-------------------")
time.sleep(2)
print("-----------------------------OPEN-BROWSER--------------------------------")
time.sleep(2)
try:
    #open your chrome driver
    openbrowser = webdriver.Chrome(executable_path="C:\\Users\\Vaimpier Ritik\\.wdm\\drivers\\chromedriver\\win32\\91.0.4472.101\\chromedriver.exe")
    time.sleep(2)
    openbrowser.maximize_window()
    openbrowser.get("https://instagram.com")
    time.sleep(2)
    engine.say("Instagram opened SUCCESSFULLY")
    engine.runAndWait()
    #database
    takeusername = openbrowser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
    takepassw = openbrowser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
    #submit(login)
    actionsub = openbrowser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")

    #give data >>>>>>>>>
    takeusername.send_keys(usrname)
    time.sleep(1)
    takepassw.send_keys(passwd)
    time.sleep(1)
    actionsub.click()
    time.sleep(7)

    engine.say(usrname +"is SUCCESSFULLY login")
    engine.runAndWait()

    #now let's start >>>>>> 
    notnow = openbrowser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
    notnow.click()
    time.sleep(4)
    notnowtwo = openbrowser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
    notnowtwo.click()
    time.sleep(2)

    #action here with vicitm name
    openbrowser.get("https://www.instagram.com/"+ vicitmname)
    time.sleep(1)
    engine.say("Finding"+ vicitmname +"SUCCESSFULLY")
    engine.runAndWait()
    openbrowser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[1]/div/div[1]/div/button").click()
    time.sleep(7)

    #open inbox
    #cvbm = openbrowser.find_element_by_class_name("xWeGp").click()
    #time.sleep(2)
    #open first conversation
    #openbrowser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a/div").click()



    while True:
        touchmsg = openbrowser.find_element_by_tag_name('textarea')
        touchmsg.send_keys(random.choice(list))
        touchmsg.send_keys(Keys.ENTER)
        #engine.say("Message are sent successfully to"+ vicitmname)
        #engine.runAndWait()
        time.sleep(0.1)
except:
    print("------------------------WTF?-IS-THIS------------------------")
    engine.say("what the fuck it is please try again why you going wrong path")
    engine.runAndWait()
    try:
        openbrowser.get("jbsnhacking.simdif.com")
     #Mr.H4cker
        engine.runAndWait()
    except:
        sys.exit("HAVE A GOOD DAY")
