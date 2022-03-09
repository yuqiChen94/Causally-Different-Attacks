import os
import numpy as np
import time
from sklearn import svm
import datetime
import joblib
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
def data_proess(x_path,y_path):
    X = np.load(x_path, allow_pickle=True)
    Y = np.load(y_path, allow_pickle=True)
    X = X[100:X.shape[0] - 1]
    Y = Y[100:]
    X_train, X_test, y_train, y_test = train_test_split(X, Y)
    return X_train, X_test, y_train, y_test

def data_proess_lit101(x_path,y_path):
    X = np.load(x_path, allow_pickle=True)
    Y = np.load(y_path, allow_pickle=True)
    X = X[100:X.shape[0] - 1]
    Y = Y[100:]
    newX = []
    for i in range(0, len(X)):
        newX.append(list(X[i][0:3]))

    newX=np.array(newX)
    X_train, X_test, y_train, y_test = train_test_split(newX, Y)
    return X_train, X_test, y_train, y_test


def SVR_rbf_training(X_train,y_train,model_path):
    clf= SVR(kernel='rbf', C=1, gamma=1).fit(X_train,y_train)
    joblib.dump(clf, model_path)

def SVR_linear_training(X_train,y_train,model_path):
    clf= SVR(kernel='linear').fit(X_train,y_train)
    joblib.dump(clf, model_path)

def evaluation(X_test,y_test,model_path):
    clf=joblib.load(model_path)
    # clf.predict_proba(X_test[:1])
    print(clf.score(X_test, y_test))


starttime = datetime.datetime.now()
x_path="training_data/x_lit101.npy"
y_path="training_data/y_lit101.npy"
model_path="prediction_model/svm_model"
model_path_linear="prediction_model/linear_model"
interval=1

X, X_test, y, y_test=data_proess_lit101(x_path,y_path)

# print (y[:100]
# # print (len(X[0]))
# # print (y)

# SVR_rbf_training(X,y,model_path)
print (len(X_test))
evaluation(X_test,y_test,model_path)

# SVR_linear_training(X,y,model_path_linear)
# evaluation(X_test,y_test,model_path_linear)


#long running
#do something other
endtime = datetime.datetime.now()
print ((endtime - starttime).microseconds)
