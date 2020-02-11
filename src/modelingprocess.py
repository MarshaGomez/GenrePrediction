from nt import listdir
import pandas as pd
import nltk
import csv

GENERE= 'Puzzle'

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

noTagsVector = []
#modify genre tags: one vs others
train = games_new
num_reviews = 10
clean_train_reviews = []

# for i in range(0, num_reviews):
  #  clean_train_reviews.append(train["description"][i])
    

flag=0
i = 0
for tag in train['genre_new']:
    tagVector = [0,0,0,0,0,0,0,0,0,0,0,0]

    #print(tag)
    #for gen in tag:
    for tagOne in tag:
        #print(tag)
        #print(gen)
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

    for noTags in tagVector:
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
df.head(20)
export_csv = df.to_csv (r'./binaryNoOneGenre.csv', index = None, header=True)

print (df)
