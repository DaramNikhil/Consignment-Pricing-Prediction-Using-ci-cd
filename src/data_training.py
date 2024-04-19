import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, r2_score
from sklearn.neighbors import KNeighborsRegressor


class Model_Training:
    def __init__(self, main_data):
        self.main_data = main_data
        self.X = self.main_data[:, :-1]
        self.y = self.main_data[:, -1]

    def LinerRegression(self):
        self.model = LinearRegression()
        self.model.fit(self.X, self.y)
        pred = self.model.predict(self.X)
        r2_score_ = r2_score(self.y, pred)
        return r2_score_

    def KNeighborsRegressor(self):
        self.model2 = KNeighborsRegressor(n_neighbors=5, metric="minkowski")
        self.model2.fit(self.X, self.y)
        pred = self.model2.predict(self.X)
        r2_score_ = r2_score(self.y, pred)
        return r2_score

    def DecisionTreeRegressor(self):
        self.model3 = DecisionTreeRegressor(criterion="squared_error", random_state=1)
        self.model3.fit(self.X, self.y)
        pred = self.model3.predict(self.X)
        r2_score_ = r2_score(self.y, pred)
        return r2_score_

    def SVR(self):
        self.model4 = SVR(kernel="rbf")
        self.model4.fit(self.X, self.y)
        pred = self.model4.predict(self.X)
        r2_score_ = r2_score(self.y, pred)
        return r2_score_

    def Best_model(self):
        liner_r = self.LinerRegression()
        Kn_r = self.KNeighborsRegressor()
        dt_r = self.DecisionTreeRegressor()
        svr = self.SVR()
        model_scores = {
            "Linear Regression": liner_r,
            "Kneighbors Classifier": Kn_r,
            "Decision Tree": dt_r,
            "SVR": svr,
        }
        return model_scores


def Model_trainings_Process_post(data):
    Model_Training_obj = Model_Training(main_data=data)
    model_scores = Model_Training_obj.Best_model()
    print(model_scores)
