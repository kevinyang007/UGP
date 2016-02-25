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

def get_sublist(indexes, lst):
    ret = []
    for index in indexes:
        ret.append(lst[index])
    return ret

try:
    with open('caltech_images.out') as f:
        X = [int(x.strip('\n')) for x in f.readlines()]
    with open('caltech_labels.out') as f:
        Y = [int(x.strip('\n')) for x in f.readlines()]
    
except IOError:     # Data not already formatted, manually format and dump in files
    print('Data not found... Creating Data:')
    X=[]    # Image 
    Y=[]    # Corresponding Label
    rootdir = '../Datasets/Caltech/101_ObjectCategories'
    for dirpath, dirnames, filenames in os.walk(rootdir):
        for file in filenames:
            file= os.path.join(dirpath, file)
            array=ndimage.imread(file,mode='RGB')
            vector=[]
            for row in range(0,300):
                for column in range(0,300):
                    for j in range(0,3):
                        try:		
                            vector.append(array[row,column,j])
                        except IndexError:
                            vector.append(0)
            X.append(vector)
            Y.append(dirpath)
    try:
        file_img = open('caltech_images.out','wb')
        for item in X:
            print >> file_img, item
        file_lbl = open('caltech_labels.out','wb')
        for item in Y:
            print >> file_lbl, item
    except Exception as e:
        print 'Unable to save data to files'
        pass
  
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
