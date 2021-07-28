"""
This script will post a new message everyday on Skype
"""
import datetime, os, random, time
import text_const
import schedule

from skpy import Skype

#Channels
Qxf2_Main='19:5232f2512c9d4fe7bd50afa86a25df69@thread.skype'
SKYPE_USERNAME = ""
SKYPE_PASSWORD = ""

scheduleTimeMessage = {
    text_const.FIX_START_MORNING_WORKING_TIME : text_const.FIX_START_MORNING_WORKING_MESSAGE,
    text_const.FIX_END_MORNING_WORKING_TIME : text_const.FIX_END_MORNING_WORKING_MESSAGE,
    text_const.FIX_START_AFTERNOON_WORKING_TIME : text_const.FIX_START_AFTERNOON_WORKING_MESSAGE,
    text_const.FIX_END_AFTERNOON_WORKING_TIME : text_const.FIX_END_AFTERNOON_WORKING_MESSAGE,
}

def get_message():
    "Return a suitable message based on the day of the week"
    return configs.START_MORNING_WORKING_MESSAGE

def post_message(msg):
    "Post a message"
    print ("I'm working...", msg)
    sk = Skype(SKYPE_USERNAME,SKYPE_PASSWORD)
    # channel = sk.chats.recent()
    # print(channel)
    channel = sk.chats.chat(Qxf2_Main)
    channel.sendMsg(msg)

#----START OF SCRIPT
if __name__=='__main__':
    # post_todays_message()
    for key in scheduleTimeMessage:
        print(key, "__", scheduleTimeMessage[key])
        schedule.every().day.at(key).do(post_message, scheduleTimeMessage[key])

    while True:
        schedule.run_pending()
    time.sleep(60)

