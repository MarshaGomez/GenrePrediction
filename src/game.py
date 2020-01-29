import rawgpy
import time
import json
import urllib.request
from nt import listdir
import os
import re
from os import path
import csv

class Game():

    def __init__(self, **kwargs):
        self.starting_url = kwargs.get('starting', 'https://api.rawg.io/api/games')
        self.directory = kwargs.get('dir', 'GamesPrev')
        self.rawg = rawgpy.RAWG("User-Agent, this should identify your app")

    def cleandataset(self):
        #csv
        #with open('games.csv', mode='w') as games_file:
        #    games_writer = csv.writer(games_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #    games_writer.writerow(["id","name", "description", "genres"])

        files = (listdir("./Cleaned_dataset"))
        for file in files:
            with open("./Cleaned_dataset/"+file) as f:
                print(f)
                gameinfo={}
                game = json.load(f)

                if game['id'] is not None:
                    gameinfo['id']= game['id']
                
                if game['name'] is not None:
                    gameinfo['name']= game['name']
         
                if game['description_raw'] is not None:
                    gameinfo['description_raw'] = game['description_raw']
     
                if game['genres'] is not None:
                    genres= game['genres']
                    gameinfo['genres']=[]
                    for genre in genres:
                        gen=genre['name']
                        gameinfo['genres'].append(gen)
           
                json.dump(gameinfo, open("./clean.json", "a"), indent = 2)

                #
                #with open('games.csv', mode='a', encoding='utf-8') as games_file:
                #    games_writer = csv.writer(games_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                #    games_writer.writerow([gameinfo['id'], gameinfo['name'], gameinfo['description_raw'], gameinfo['genres']])



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # alcuni giochi non hanno il genere, quindi è inutile metterli nel csv, 
            # poi decidere se pulire la descrizione prima di metterla nel csv, 
            # decidere se lasciare l'id
            