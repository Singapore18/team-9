from pymongo import MongoClient
from pymongo import cursor
import pymongo

import pandas as pd

import json
import itertools
import collections

file = "rawQuestions.csv"

client = MongoClient("mongodb://randylai.2016:JpmcfgTeam9@ds129823.mlab.com:29823/jpcfg")
db = client.jpcfg

dataFrame = pd.read_csv(file)

dict = dataFrame.to_dict('records')

dfList = list(dataFrame)

collection = db.ExactQuestion

for x in dict:
    question = x[dfList[0]]
    rScore = x[dfList[1]]
    score = True
    
    if rScore == "No":
        score = False
        
    record = {
        "question" : question,
        "rScore" : score
    }
    
    collection.insert_one(record)
    
client.close()