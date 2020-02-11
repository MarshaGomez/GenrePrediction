from nt import listdir
import pandas as pd
import nltk
import csv

def getBinaryGenreTag(games_new):
    train = games_new

    clean_train_reviews = []
    tagVector = []
    i = 0

    for tag in train['genre_new']: 
        clean_train_reviews.append(train["description"][i])
        tagVector.append(tag[0])
        i = i + 1

    data = {'plot': clean_train_reviews, 'tags': tagVector}
    df = pd.DataFrame(data)
    export_csv = df.to_csv (r'./data/binaryOneGenre.csv', index = None, header=True)

    print ('Process Finish. getBinaryGenreTag()')

def getBinaryOtherTags(games_new):
    train = games_new
    clean_train_reviews = []
    noTagsVector = []

    i = 0
    for tag in train['genre_new']:
        tagVector = [0,0,0,0,0,0,0,0,0,0,0,0]

        for tagOne in tag:
            if tagOne =='Sports':
                tagVector[0] = 1
            if tagOne =='Fighting':
                tagVector[1] = 1
            if tagOne =='Educational':
                tagVector[2] = 1
            if tagOne =='Puzzle':
                tagVector[3] = 1
            if tagOne =='BoardGames':
                tagVector[4] = 1
            if tagOne =='Adventure':
                tagVector[5] = 1
            if tagOne =='Action':
                tagVector[6] = 1
            if tagOne =='RPG':
                tagVector[7] = 1
            if tagOne =='Simulation':
                tagVector[8] = 1
            if tagOne =='Strategy':
                tagVector[9] = 1
            if tagOne =='Shooter':
                tagVector[10] = 1
            if tagOne =='Racing':
                tagVector[11] = 1

        if tagVector[0] != 1:
            clean_train_reviews.append(train["description"][i])
            noTagsVector.append('Sports')
        if tagVector[1] != 1:
            clean_train_reviews.append(train["description"][i])
            noTagsVector.append('Fighting')
        if tagVector[2] != 1:
            clean_train_reviews.append(train["description"][i])
            noTagsVector.append('Educational')
        if tagVector[3] != 1:
            clean_train_reviews.append(train["description"][i])
            noTagsVector.append('Puzzle')
        if tagVector[4] != 1:
            clean_train_reviews.append(train["description"][i])
            noTagsVector.append('BoardGames')
        if tagVector[5] != 1:
            clean_train_reviews.append(train["description"][i])
            noTagsVector.append('Adventure')
        if tagVector[6] != 1:
            clean_train_reviews.append(train["description"][i])
            noTagsVector.append('Action')
        if tagVector[7] != 1:
            clean_train_reviews.append(train["description"][i])
            noTagsVector.append('RPG')
        if tagVector[8] != 1:
            clean_train_reviews.append(train["description"][i])
            noTagsVector.append('Simulation')
        if tagVector[9] != 1:
            clean_train_reviews.append(train["description"][i])
            noTagsVector.append('Strategy')
        if tagVector[10] != 1:
            clean_train_reviews.append(train["description"][i])
            noTagsVector.append('Shooter')
        if tagVector[11] != 1:
            clean_train_reviews.append(train["description"][i])
            noTagsVector.append('Racing')
        
        i = i + 1
    

    data = {'plot': clean_train_reviews, 'tags': noTagsVector}
    df = pd.DataFrame(data)
    export_csv = df.to_csv (r'./data/binaryOtherTags.csv', index = None, header=True)

    print ('Process Finish. getBinaryOtherTags()')

def initProcess():
    pd.set_option('display.max_colwidth', 300)
    meta = pd.read_csv("./data/gameClean.csv", sep = ',' , header = None)

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

    games['genre_new'] = genres
    games_new =  games[~(games['genre_new'] == ' ')]

    # getBinaryGenreTag(games_new)
    # print('Task Complete getBinaryGenreTag')

    getBinaryOtherTags(games_new)
    print('Task Complete getBinaryOtherTags')


initProcess()
