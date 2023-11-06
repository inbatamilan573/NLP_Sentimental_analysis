import pandas as pd

df =  pd.read_csv('F:/Forsk/balanced_reviews_.csv')



df.isnull().any(axis = 0)

#handle the missing data
df.dropna(inplace =  True)

#leaving the reviews with rating 3 and collect reviews with
#rating 1, 2, 4 and 5 onyl

df = df [df['overall'] != 3]

import numpy as np

#creating a label
#based on the values in overall column
df['Positivity'] = np.where(df['overall'] > 3 , 1 , 0)
#data cleaning

import nltk
import re
nltk.download('stopwords')

from nltk.stem.porter import PorterStemmer

from nltk.corpus import stopwords

corpus=[]
for i in range(0,df.shape[0]):
 
    review=re.sub("[^a-zA-Z]"," ", df.iloc[i,1])
    review=review.lower()
    review=review.split()
    review = [word for word in review if not word in stopwords.words('english')]
    ps=PorterStemmer()
    review=[ps.stem(word) for word in review ]
    review=" ".join(review)
    corpus.append(review)
corpus
#tfif
from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(corpus, df['Positivity'], random_state = 42 )



from sklearn.feature_extraction.text import TfidfVectorizer

vect = TfidfVectorizer(min_df=5).fit(features_train)

features_train_vectorized = vect.transform(features_train)


#features_train_vectorized.toarray()


#create the classifier (first model)

#SVC,KNN, Naive Bayes, Logistic Regression, DT, RF


from sklearn.linear_model import LogisticRegression


model = LogisticRegression(max_iter=10000)

model.fit(features_train_vectorized, labels_train)

predictions = model.predict(vect.transform(features_test))


from sklearn.metrics import confusion_matrix

confusion_matrix(labels_test, predictions)

from sklearn.metrics import roc_auc_score
roc_auc_score(labels_test, predictions)

#pickle
import pickle
file =open("pickle_model_final.pkl","wb")

pickle.dump(model, file)

#vect vacobalary
pickle.dump(vect.vocabulary_,open("features_final.pkl","wb"))







