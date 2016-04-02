from mnist import MNIST
from sklearn.externals import joblib
from sklearn import datasets
from skimage.feature import hog
from sklearn.svm import LinearSVC
import numpy as np
from random import shuffle

from sklearn.cross_validation import cross_val_score
from sklearn.tree import DecisionTreeClassifier

def preprocessData():
    lst = [i[0] for i in sorted(enumerate(labels), key=lambda x:x[1])]
    sorted_X = []
    sorted_y = []
    for i in range(0,len(lst)):
        sorted_X.append(features[lst[i]])
        sorted_y.append(labels[lst[i]])

    start_points = [0]
    j = 0
    for i in range(0,len(sorted_y)):
        if(sorted_y[i]!=j):
            start_points.append(i)
            j = sorted_y[i]
    start_points.append(70000)
    X_train = [] 
    X_test = []
    y_train = []
    y_test = []
    for i in range(0,len(start_points)-1):
        lst_X = lst_y = []
        l = start_points[i]
        r = start_points[i+1]
        lst_X = sorted_X[l:r]
        lst_y = sorted_y[l:r]
        shuffle(lst_X)
        shuffle(lst_y)
        temp_X = lst_X[0:1000]
        temp_y = lst_y[0:1000]
        X_train = X_train+temp_X
        y_train = y_train+temp_y
        temp_X = lst_X[1001:1101]
        temp_y = lst_y[1001:1101]
        X_test = X_test+temp_X
        y_test = y_test+temp_y

    shuffle(X_train)
    shuffle(y_train)
    shuffle(X_test)
    shuffle(y_test)
    return X_train, y_train, X_test, y_test

def loaddata():
    #Loading mnist data using python-mnist library
    mnLoader = MNIST('asgndata/mnist')
    data1 = mnLoader.load_training() # train data
    data2 = mnLoader.load_testing()  # test data

    features = np.array(data1[0]+data2[0], 'int16')
    labels = np.array(data1[1]+data2[1], 'int')
    X_train, y_train, X_test, y_test = preprocessData(features, labels)
    return X_train, y_train, X_test, y_test 

def getHog(X_train):
    list_hog_fd = []
    i = 0
    for feature in X_train:
        fd = hog(feature.reshape((28, 28)), orientations=9, pixels_per_cell=(14, 14), cells_per_block=(1, 1), visualise=False)
        list_hog_fd.append(fd)
    X_train = np.array(list_hog_fd, 'float64') 
    return X_train

X_train, y_train, X_test, y_test = loaddata()
X_train = getHog(X_train) 
X_test = getHog(X_test) 

clf = DecisionTreeClassifier(random_state=0)
print cross_val_score(clf, hog_features, labels, cv=2)
