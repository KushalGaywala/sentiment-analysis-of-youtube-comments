from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
import nltk
from nltk.stem import LancasterStemmer
from nltk.stem import WordNetLemmatizer
import pandas as pd
import argparse
from train import load_dataset

youtube_data = load_dataset()
comments_train, comments_test, sentiment_train, sentiment_test = train_test_split(
    youtube_data,
    test_size=0.25,
    random_state=42,
)

pipeline = Pipeline([('vect', TfidfVectorizer()), ('clf', LinearSVC())])
param_grid = {
    'vect__ngram_range': [(1, 1), (1, 2)],
    'vect__sublinear_tf': [False, True],
}

grid_search_cv = GridSearchCV(pipeline, param_grid)
best_model = grid_search_cv.fit(youtube_data.loc[:, 'comments'], youtube_data.loc[:, 'sentiment'])
test_accuracy = best_model.score(comments_test, sentiment_test)

pd.DataFrame(grid_search_cv.cv_results_).to_csv('training_results_different_hyperparameters.csv')

print("Training finished")
print(f"Final model as test accuracy of {test_accuracy:2%}.")