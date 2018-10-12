from pymongo import MongoClient
from pymongo import cursor
import pymongo

import pandas as pd

import json
import itertools
import collections

file = "Workshop data cleaned.xlsx"

client = MongoClient("mongodb://randylai.2016:JpmcfgTeam9@ds129823.mlab.com:29823/jpcfg")
db = client.jpcfg

dataFrame = pd.read_excel(file)

dict = dataFrame.to_dict('records')

dfList = list(dataFrame.columns.values)

qnCollection = db.ExactQuestion

collection = db.CleanedData

table = qnCollection.find()

for x in dict:
    for item in table:
        rScore = item["rScore"]
        if rScore:
            question = item["question"]
            if question in dfList:
                value = x[question]
                if value == 1:
                    value = 7
                elif value == 2:
                    value = 6
                elif value == 3:
                    value = 5
                elif value == 5:
                    value = 3
                elif value == 6:
                    value = 2
                elif value == 7:
                    value = 1
                x[question] = value
    
    collection.insert(x,check_keys=False)
    
    
client.close()
        
    
    

        
