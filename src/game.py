import rawgpy
import time
import json
import urllib.request
from nt import listdir
import os
import re
from os import path
import numpy as np
import nltk
import csv
import matplotlib.pyplot as plt 
import seaborn as sns
from tqdm import tqdm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
import pandas as pd
from langdetect import detect
import sys
import warnings


# nltk.download('stopwords')
# nltk.download('punkt')
with open('gameClean.csv', mode='w') as games_file:
    games_writer = csv.writer(games_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    games_writer.writerow(["id","name","descr", "genres"])

    files = (listdir("C:/Users/Matilde/Desktop/dataminingprog/Cleaned_dataset"))
    for file in files:
        with open("C:/Users/Matilde/Desktop/dataminingprog/Cleaned_dataset/"+file) as f:
            gameinfo = {}
            game = json.load(f)

            if game['genres'] != []:
                if game['description_raw'] is not None and len(game['description_raw']) > 50:
                    desc = game['description_raw']
                elif game['description'] is not None:
                    desc = game['description']

                if desc != '' and len(desc)>50:
                    if game['id'] is not None or game['id'] != '':
                        gameinfo['id']= game['id']
                    
                    if game['name'] is not None or game['name'] != '':
                        # print(game['name'])
                        name = game['name']
                        name = re.sub("\'", "", name) 
                        name= name.replace(",",'').replace("\n", " ")
                        name = re.sub("[^a-zA-Z\d ]"," ", name) 
                        name = name.lower() 
                        
                        # remove everything except alphabets 
                        
                        # remove whitespaces 
                        name = ' '.join(name.split())
                        name = name.strip()

                        descri = re.sub(r'http\S+', '', desc, flags=re.MULTILINE)
                        descri = descri.lower() 
                        descri= descri.replace(",",'').replace("\n", " ")
                        
                        descri = re.sub("\'", "", descri) 
                        # remove everything except alphabets 
                        descri = re.sub("\b\w{0,2}\b|[^a-zA-Z ]"," ", descri) 
                        
                        # remove whitespaces 
                        descri = ' '.join(descri.split())
                        descri = descri.strip()
                    
                        stop_words = set(stopwords.words('english'))
                        # print(stop_words)
                        
                        word_tokens = word_tokenize(descri)
                        # print(word_tokens)

                        filtered_sentence = [w for w in word_tokens if not w in stop_words] 
                        
                        filtered_sentence = [] 
                        
                        for w in word_tokens: 
                            if w not in stop_words: 
                                filtered_sentence.append(w)
                        
                        if descri != '':
                            # print('-'+name+'-'+descri+'-')
                            lang = detect(descri)
                            
                            if lang != 'en':
                                descri=''
                                #print(lang)
                                #print(f)
                            else:
                                stemmer = SnowballStemmer('english')
                                stemSentence = ''
                                for word in filtered_sentence:
                                    stem = stemmer.stem(word)
                                    stemSentence += stem
                                    stemSentence += " "

                                descri = re.sub("\\b\\w{0,2}\\b|[^a-zA-Z ]"," ", str(stemSentence))
                                    # remove whitespaces 
                                descri = ' '.join(descri.split())
                                descri = descri.strip()


                        genres= game['genres']
                        gameinfo['genres']=[]
                        #gameinfo['genres_new']=[]
                        for genre in genres:
                            flag=False                    
                            gen=genre['name']

                            if gen == 'Massively Multiplayer':
                                gen = 'RPG'

                            if gen == 'Card':
                                gen = 'Board Games'

                            if gen != 'Platformer' and gen != 'Family' and gen != 'Casual' and gen != 'Indie' and gen != 'Arcade':
                                gameinfo['genres'].append(gen)
                                #gameinfo['genres_new'].append(gen)
                            #else:
                                #gameinfo['genres_new'].append(gen)
                                #flag=True
                            
                            
                        #gameinfo['genres_new'] = list(dict.fromkeys(gameinfo['genres_new']))
                        gameinfo['genres'] = list(dict.fromkeys(gameinfo['genres']))
                        
                
                    #json.dump(gameinfo, open("./clean.json", "a"), indent = 2)

                    if descri != '' and name != '' and flag ==False and gameinfo['genres'] != []:
                        # print(game['id'])
                        with open('bigData.csv', mode= 'a', encoding='utf-8') as games_file:
                            games_writer = csv.writer(games_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                            games_writer.writerow([gameinfo['id'], name, descri, gameinfo['genres']])
                    # elif  descri != '' and name != '' and flag ==True:
                        # print(game['id'])
                        # with open('gameTest.csv', mode= 'a', encoding='utf-8') as games_file:
                            # games_writer = csv.writer(games_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                            # games_writer.writerow([gameinfo['id'], name, descri, gameinfo['genres_new']])

