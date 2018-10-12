from pymongo import MongoClient
from pymongo import cursor
import pymongo

import pandas as pd

import json
import itertools
import collections

file = "questions.csv"

client = MongoClient("mongodb://randylai.2016:JpmcfgTeam9@ds129823.mlab.com:29823/jpcfg")
db = client.jpcfg

dataFrame = pd.read_csv(file)

dict = dataFrame.to_dict('records')

dfList = list(dataFrame)

qDict = {}

for x in dict:
    keystone = x[dfList[0]]
    metric = x[dfList[1]]
    qnNum = str(x[dfList[2]])
    question = x[dfList[3]]
    rScore = x[dfList[4]]
    
    if not keystone in qDict:
        kDict = {}
        qList = []
        qnDict = {}
        qnDict[qnNum] = { "question" : question, "rScore" : rScore}
        qList.append(qnDict)
        kDict[metric] = qList
        qDict[keystone] = kDict
        
    else:
        kDict = qDict[keystone]
        if metric in kDict:
            qnDict = {}
            qnDict[qnNum] = { "question" : question, "rScore" : rScore}
            qList.append(qnDict)
            kDict[metric] = qList
            qDict[keystone] = kDict
        else:
            kDict = {}
            qList = []
            qnDict = {}
            qnDict[qnNum] = { "question" : question, "rScore" : rScore}
            qList.append(qnDict)
            kDict[metric] = qList
            qDict[keystone] = kDict
            
collection = db.Questions
try:
    collection.insert_one(qDict)
except Exception as e:
    print(str(e))

client.close()

        