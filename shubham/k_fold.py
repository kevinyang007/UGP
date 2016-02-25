from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import KFold
from sklearn.metrics import confusion_matrix, f1_score
from sklearn.pipeline import Pipeline

from scipy import ndimage
from sklearn import svm
import numpy as np
from sklearn.feature_extraction import image
import os
import sys
import matplotlib.pyplot as plt
import pickle # For loading and storing list to a file
import numpy
from sklearn.metrics import accuracy_score


def get_sublist(indexes, lst):
    ret = []
    for index in indexes:
        ret.append(lst[index])
    return ret

X=[[1,2,3,4],[5,6,7,8],[9,1,2,3],[4,5,6,7]]
Y=[1,2,3,4]

clf = svm.SVC()
pipeline = Pipeline([('svc', clf )])

k_fold = KFold(n=len(X), n_folds=2)
scores = []

for train_indices, test_indices in k_fold:
    train_img = get_sublist(train_indices, X) 
    train_y = get_sublist(train_indices, Y)

    test_img = get_sublist(test_indices, X) 
    test_y = get_sublist(test_indices, Y) 

    pipeline.fit(train_img, train_y)
    predictions = pipeline.predict(test_img)
    score = accuracy_score(test_y, predictions)
    scores.append(score)

print('Total images classified:', len(X))
print('Score:', sum(scores)/len(scores))
print scores

