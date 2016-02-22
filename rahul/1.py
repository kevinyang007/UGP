from scipy import ndimage
from sklearn import svm
import numpy as np
from sklearn.feature_extraction import image
import os
import sys
rootdir = '/home/rahul/Downloads/101_ObjectCategories'
X=[]
Y=[]
for subdir, dirs, files in os.walk(rootdir):
    i=0
    for file in files:
        if i>=0 and i<15:
            i+=1
        else:
            continue
        file= os.path.join(subdir, file)
        array=ndimage.imread(file,mode='RGB')
        vector=[]
        for row in range(0,200):
            for column in range(0,300):
                for j in range(0,3):
                    vector.append(array[row,column,j])
        X.append(vector)
        Y.append(subdir)
clf = svm.SVC()
clf.fit(X, Y)
true=0
false=0
for subdir, dirs, files in os.walk(rootdir):
    i=0
    for file in files:
        i+=1
        if not (i>=16 and i<=20):
            continue
        file= os.path.join(subdir, file)
        array=ndimage.imread(file,mode='RGB')
        vector=[]
        for row in range(0,200):
            for column in range(0,300):
                for j in range(0,3):
                    vector.append(array[row,column,j])
        test=[vector]
        if clf.predict(test)[0]==subdir:
            true+=1
        else:
            false+=1
print true/(true+false)