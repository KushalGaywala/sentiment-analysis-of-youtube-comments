import joblib

import pandas as pd
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

from elastic_search_API import elasticSearchAPI


def load_dataset() -> pd.DataFrame:
    youtube_mapping = {
        "dynamic": "strict",
        "properties": {
            "sentiment":    {"type": "text"},
            "comment":  {"type": "keyword"},
        }
    }
    # TODO: rename to YouTube
    es_API = elasticSearchAPI("youtube_reviews", youtube_mapping)
    return es_API.load_reviews()

youtube_data = load_dataset()
comments_train, comments_test, sentiment_train, sentiment_test = train_test_split(
    youtube_data,
    test_size=0.25,
    random_state=42,
)

pipeline = Pipeline([('vect', TfidfVectorizer(sublinear_tf=True)), ('clf', LinearSVC())])

pipeline.fit(youtube_data.loc[:, 'comment'], youtube_data.loc[:, 'sentiment'])
test_accuracy = pipeline.score(comments_test, sentiment_test)

joblib.dump(pipeline, './youtube_model.joblib')

print("Training finished")
print(f"Final model as test accuracy of {test_accuracy:2%}.")
