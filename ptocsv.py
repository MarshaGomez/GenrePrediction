import rawgpy
import time
import json
import urllib.request
from nt import listdir
import os
import re
from os import path
import pandas as pd
import numpy as np
import nltk
import csv
import matplotlib.pyplot as plt 
import seaborn as sns
from tqdm import tqdm
from sklearn import svm
from sklearn import linear_model
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.linear_model import LogisticRegression
# Binary Relevance
from sklearn.multiclass import OneVsRestClassifier
# Performance metric
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier

GENERE= 'Puzzle'

pd.set_option('display.max_colwidth', 300)
meta = pd.read_csv("./bigData.csv", sep = ',' , header = None)

meta.columns = ["id","name","description","genres"]

games = pd.DataFrame(meta)
games.head()
print(games)
genres = [] 
genres1 = [] 
s1= ['']
# extract genres
for i in games['genres']: 
    a = list(i.replace("]",'').replace('[','').replace("'",'').replace(' ','').split(","))
    if a == s1:
        genres.append(' ') 
    else:
        genres.append(a)
        genres1.append(a)

# add to 'movies' dataframe  
games['genre_new'] = genres
games.shape
games_new =  games[~(games['genre_new'] == ' ')]
games_new.head(1000)

all_genres = sum(genres1,[])
print(len(set(all_genres)))
all_genres = nltk.FreqDist(all_genres) 

# create dataframe
all_genres_df = pd.DataFrame({'Genre': list(all_genres.keys()), 
                              'Count': list(all_genres.values())})
print(list(all_genres.keys()))


#modify genre tags: one vs others
train = games_new
num_reviews = 10
clean_train_reviews = []

# for i in range(0, num_reviews):
  #  clean_train_reviews.append(train["description"][i])
    

tagVector = []
flag=0
i = 0
for tag in train['genre_new']: 
    #print(tag)
    for gen in tag:
        clean_train_reviews.append(train["description"][i])

        #print(tag)
        #print(gen)
        if gen == 'Puzzle':
            tagVector.append('Puzzle')
        if gen =='Adventure':
            tagVector.append('Adventure')   
        if gen =='Action':
            tagVector.append('Action')   
        if gen =='RPG':
            tagVector.append('RPG')   
        if gen =='Simulation':
            tagVector.append('Simulation')   
        if gen =='Strategy':
            tagVector.append('Strategy')   
        if gen =='Shooter':
            tagVector.append('Shooter')   
        if gen =='Sports':
            tagVector.append('Sports')   
        if gen =='Racing':
            tagVector.append('Racing')   
        if gen =='Educational':
            tagVector.append('Educational')  
        if gen =='Fighting':
            tagVector.append('Fighting')   
        if gen =='BoardGames':
            tagVector.append('BoardGames')   
    i = i + 1


data = {'plot': clean_train_reviews, 'tags': tagVector}
df = pd.DataFrame(data)
df.head(20)
#print (df)
"""
delete_row = df[df.iloc[:,1]=='other'].index
#print(delete_row)
 

df = df.drop(delete_row[3000:40000])
print(delete_row)
"""
export_csv = df.to_csv (r'./binaryOneGenre.csv', index = None, header=True)

print (df)
