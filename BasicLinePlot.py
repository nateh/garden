#!/usr/bin/env python
# coding: utf-8



import os
#from pprint import pprint
#import bson
from dotenv import load_dotenv
import dotenv
import pymongo
from pymongo import MongoClient
import plotly_express as px
import datetime
import pandas as pd




# Load config from a .env file:
load_dotenv(verbose=True)
MONGODB_URI = os.environ["MONGODB_URI"]

# Connect to your MongoDB cluster:
client = pymongo.MongoClient(MONGODB_URI)

# Get a reference to the "sample_mflix" database:
db = client["growing"]

# Get a reference to the "movies" collection:
movie_collection = db["weather"]





stage_match_title = {
   "$match": {
         "name": "Greensborough"
   }
}
# # Sort by year, ascending:
stage_sort_year_ascending = {
    "$sort": { "dt": pymongo.ASCENDING }
 }
stage_limit_1 = { "$limit": 100 }    
pipeline = [
    stage_match_title, 
    stage_sort_year_ascending,
    # Limit to 1 document:
    stage_limit_1,
 ]
results = movie_collection.aggregate(pipeline)




my_list=[]
for movie in results:
    #my_list.append(datetime.datetime.fromtimestamp(movie["dt"]))
    #my_list.append(movie["main"]["temp"])
    my_list.append([datetime.datetime.fromtimestamp(movie["dt"]),movie["main"]["temp"]])

df = pd.DataFrame(my_list)



#print(df)



print(df[0])




basic_line_plot = px.line(x=df[0],y= df[1], title="Basic Line Plot")
basic_line_plot.show()

