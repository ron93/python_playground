import pandas as pd 
import numpy as np

from sklearn import ensemble
from sklearn import metrics 
from sklearn import model_selection
from pathlib import Path


if __name__ == "__main__":
    data_folder = Path("../data/mobile-price/")

    f = data_folder / "train.csv"
    df = pd.read_csv(f)
    #train
    X = df.drop("price_range",axis=1).values
    y = df.price_range.values

    #n_jobs = -1 ->to use all available processing availabel
    classifier = ensemble.RandomForestClassifier(n_jobs=-1)

    param_grid = {
        "n_estimators": np.arange(100,1500,100),
        "max_depth" :np.arange(1,20),
        "criterion" : ["gini","entropy"],
    }


    #cv(cross validation) -> 5 fold
    model = model_selection.RandomizedSearchCV(
        estimator = classifier,
        param_distributions=param_grid,
        scoring="accuracy",
        n_iter=10,
        verbose=10,
        n_jobs=1,
        cv=5,
    )

    model.fit(X,y)

    print(model.best_score_)
    print(model.best_estimator_.get_params())