import json
from nt import listdir
import re
import os
from os import path
import csv
import matplotlib.pyplot as plt 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
import pandas as pd
from langdetect import detect

# Clean Name attribute
def cleanName(name):
    name = re.sub("[^a-zA-Z\d ]"," ", name)

    if name != '':
        name = name.lower() 
        name = ' '.join(name.split())

        return name
    else:
        return ''

# Clean Description attribute. Apply stopwords and stem
def cleanDescription(description):
    description = re.sub(r'http\S+', '', description, flags=re.MULTILINE)
    description = description.lower() 
    description = re.sub("\\b\\w{0,2}\\b|[^a-zA-Z ]"," ", description) 
    description = re.sub("([^a-zA-Z\\s+\\w]|\\s+)", " ", str(description))

    if description != ' ' and description != '':
        lang = detect(description)
        
        if lang == 'en':
            stop_words = set(stopwords.words('english'))
            word_tokens = word_tokenize(description)

            filtered_sentence = [] 
            for w in word_tokens: 
                if w not in stop_words: 
                    filtered_sentence.append(w)

            stemmer = SnowballStemmer('english')
            stemSentence = ''
            for word in filtered_sentence:
                stem = stemmer.stem(word)
                stemSentence += stem
                stemSentence += ' '
            description = re.sub("\\b\\w{0,2}\\b|[^a-zA-Z ]"," ", str(stemSentence))
            description = re.sub("([^a-zA-Z\\s+\\w]|\\s+)", " ", str(description))
            return description
        else:
            return ''
    else:
        return ''
    
# Clean Genres attribute
def cleanGenres(genres):
    cleanGenres = []
    for genre in genres:
        gen=genre['name']
        if gen == 'Massively Multiplayer':
            gen = 'RPG'

        if gen == 'Card':
            gen = 'BoardGames'

        if gen != 'Platformer' and gen != 'Family' and gen != 'Casual' and gen != 'Indie' and gen != 'Arcade':
            cleanGenres.append(gen)
        
    return list(dict.fromkeys(cleanGenres))

# Clean Description. 
def cleanCSVrow(gameinfo):
        with open('./data/gameClean.csv', mode= 'a', encoding='utf-8') as games_file:
            games_writer = csv.writer(games_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            games_writer.writerow([gameinfo['id'], gameinfo['name'], gameinfo['description'], gameinfo['genres']])

# Get Data Set valid values
def getDataSet():
    files = (listdir("./data/Cleaned_dataset"))
    for file in files:
        with open("./data/Cleaned_dataset/"+file) as f:
            gameinfo = {}
            game = json.load(f)
            if game['genres'] != [] and (game['id'] is not None or game['id'] != '') and (game['name'] is not None or game['name'] != ''):
                if game['description_raw'] is not None:
                    description = game['description_raw']
                elif game['description'] is not None: 
                    description = game['description']
                
                if description != '':
                    gameinfo['id']=game['id']
                    gameinfo['name']=cleanName(game['name'])
                    gameinfo['description']=cleanDescription(description)
                    gameinfo['genres']=cleanGenres(game['genres'])

                    if gameinfo['name'] != '' and gameinfo['description'] != '' and gameinfo['genres'] != []:
                        print(gameinfo['id'])
                        cleanCSVrow(gameinfo)

                        

# Create preprocessing final CSV dataset
def createCSV():
    with open('./data/gameClean.csv', mode='w') as games_file:
        games_writer = csv.writer(games_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        games_writer.writerow(["id","name","descr", "genres"])
    getDataSet()

# Init
nltk.download('stopwords')
nltk.download('punkt')
createCSV()