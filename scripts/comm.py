import json
import tkinter
import os
import updatetext
import index
import random
import datetime

now = datetime.datetime.now()
today = str(now.month)+"."+str(now.day)+"."+str(now.year)

def load():
    with open('../logs/testlog.json') as json_file:
        data = json.load(json_file)
        start = data['bot']['text']

    return data

def checkCommand(text):
    text=text.lower()
    if 'hi' in text or 'hello' in text:
        print(today)
        return ('What can I help you with?', 'TRUE')
    if "me a joke" in text:
        x = random.randint(0,2)
        y = str(x)
        with open('../logs/jokes.json') as json_file:
            data = json.load(json_file)
            start = data[y]['text']
            return (start, 'TRUE')
    if "have to do today" in text:
        with open('../logs/cal.json') as json_file:
            data = json.load(json_file)
            start = data
            return (start, 'TRUE')
    if "what is today" in text:
        return ("Today is " + today, 'TRUE')
        #TODO: Figure out how to add to cal.json
    if "do you love me" in text:
        return("nahhh u ugly", 'TRUE')
    if "add to schedule" in text:
        return("Enter the schedule to add in the following format: addsched,date,time,details,name", 'TRUE')
    if "addsched" in text:
        dataList = text.split(',')
        d = {'date':dataList[1], 'time':dataList[2], 'details':dataList[3], 'name':dataList[4]}
        with open('../logs/cal.json', mode='w', encoding='utf-8') as json_file:
            json.dump(d, json_file)
        print(d)
        return("Event added",'TRUE')
    if "test" in text:
        with open('../logs/cal.json') as json_file:
            data = json.load(json_file)
            print(data)
            return("Testing",'TRUE')
    else:
        return ("I couldnt understand what you said", 'TRUE')
