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

    genres = ['Sports', 'Fighting', 'Educational', 'Puzzle', 'BoardGames', 'Adventure', 'Action', 'RPG', 'Simulation', 'Strategy', 'Shooter', 'Racing']
    clean_train_reviews = []
    noTagsVector = []

    i = 0
    j = 0
    for tag in train['genre_new']:
        tagVector = [0,0,0,0,0,0,0,0,0,0,0,0]

        for tagOne in tag:
            j = 0
        
            for genre in genres:
                if (genre == tagOne):
                    tagVector[j] = 1
                j = j + 1
        j = 0
        for tag in tagVector:
            if tag != 1:
                clean_train_reviews.append(train["description"][i])
                noTagsVector.append(genres[j])
            j = j + 1
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

    getBinaryGenreTag(games_new)
    print('Task Complete getBinaryGenreTag')

    getBinaryOtherTags(games_new)
    print('Task Complete getBinaryOtherTags')


initProcess()
