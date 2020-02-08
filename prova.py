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



def predict(vectorizer, classifier, data):
    data_features = vectorizer.transform(data['plot'])
    predictions = classifier.predict(data_features)
    target = data['tags']
    evaluate_prediction(predictions, target)

my_tags = ['Action', 'others']
def plot_confusion_matrix(cm, title='Confusion matrix', cmap=plt.cm.Blues):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(my_tags))
    target_names = my_tags
    plt.xticks(tick_marks, target_names, rotation=45)
    plt.yticks(tick_marks, target_names)
    # plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')



def evaluate_prediction(predictions, target, title="Confusion matrix"):
    print('accuracy %s' % accuracy_score(target, predictions))
    print('precision %s' % precision_score(target, predictions,pos_label='Action'))
    print('recall %s' % recall_score(target, predictions,pos_label='Action'))
    print('f-measure %s' % f1_score(target, predictions,pos_label='Action'))

    cm = confusion_matrix(target, predictions)
    print('confusion matrix\n %s' % cm)
    print('(row=expected, col=predicted)')

    cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    plt.figure()
    plot_confusion_matrix(cm_normalized, title + ' Normalized')
    plt.show()



pd.set_option('display.max_colwidth', 300)
meta = pd.read_csv("C:/Users/Matilde/Desktop/GitHub/datamin/genrePrediction/gameCleanShort.csv", sep = ',' , header = None)

meta.columns = ["id","name","description","genres"]

games = pd.DataFrame(meta)
games.head()

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

g = all_genres_df.nlargest(columns="Count", n = 50) 
plt.figure(figsize=(12,15)) 
ax = sns.barplot(data=g, x= "Count", y = "Genre") 
ax.set(ylabel = 'Count') 
plt.show()

#modify genre tags: one vs others
train = games_new
num_reviews = 41806
clean_train_reviews = []

for i in range(0, num_reviews):
    clean_train_reviews.append(train["description"][i])

tagVector = []
for tag in train['genre_new']:
    #print(tag)
    if tag == ['Action']:
        tagVector.append('Action')
    else:
        tagVector.append('other')

data = {'plot': clean_train_reviews, 'tags': tagVector}
df = pd.DataFrame(data)
df.head(20)

"""
# knn
data_features = df

train_data, test_data = train_test_split(data_features, test_size=0.1, random_state=42)

vectorizer = TfidfVectorizer(min_df=2, tokenizer=None, preprocessor=None, stop_words=None,  max_features=10000)
train_data_features = vectorizer.fit_transform(train_data['plot'])
train_data_features = train_data_features.toarray()

knn_naive_dv = KNeighborsClassifier(n_neighbors=3, n_jobs=1, algorithm='brute', metric='cosine')
knn_naive_dv = knn_naive_dv.fit(train_data_features, train_data['tags'])
print(knn_naive_dv)
predict(vectorizer, knn_naive_dv, test_data) 
"""


#logistic regression
print('logreg')
data_features = df
train_data, test_data = train_test_split(data_features, test_size=0.2, random_state=42)

tf_vect = TfidfVectorizer(min_df=2, tokenizer=None, preprocessor=None, stop_words=None)

train_data_features = tf_vect.fit_transform(train_data['plot'])
train_data_features = train_data_features.toarray()

logreg = linear_model.LogisticRegression(n_jobs=1, C=1e5, max_iter = 100000)
logreg = logreg.fit(train_data_features, train_data['tags'])
print(logreg)
predict(tf_vect, logreg, test_data)




"""
#svm
data_features = df
train_data, test_data = train_test_split(data_features, test_size=0.1, random_state=42)

vectorizer = TfidfVectorizer(min_df=2, tokenizer=None, preprocessor=None, stop_words=None,  max_features=10000)

train_data_features = vectorizer.fit_transform(train_data['plot'])
train_data_features = train_data_features.toarray()

lin_clf = svm.LinearSVC()
lin_clf.fit(train_data_features, train_data['tags'])

predict(vectorizer, lin_clf, test_data)
"""