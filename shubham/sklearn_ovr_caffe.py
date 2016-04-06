import numpy as np
from sklearn.svm import SVC
from random import shuffle
import sys

CONST_LABELS = 5
CONST_NUMBER_TRAIN_IMG =  7500 
CONST_NUMBER_TEST_IMG =  2500 
CONST_X_FILE = '/home/cse/UGP/shubham/mlt_allX.txt'
CONST_y_FILE = '/home/cse/UGP/shubham/mlt_allimg_labels.txt'
CONST_C=[100]
CONST_KERNEL=['linear']
#C=[0.1,1,10,100,1000,10000,100000,1000000]
#kernel=['linear', 'poly', 'rbf', 'sigmoid']

def double_shuffle(a,b):
    an = []
    bn = []
    index = []
    for i in range(0,len(a)):
        index.append(i) 
    shuffle(index)
    for i in range(0,len(index)):   
        an.append(a[index[i]])
        bn.append(b[index[i]])
    return an,bn

def get_data():
	with open(CONST_X_FILE,'r') as f:
		content = f.readlines()
		X = []
		for i in range(0,len(content)):
			X.append([float(n) for n in content[i].split()])

	with open(CONST_y_FILE,'r') as f:
		content = f.readlines()
		y = []
		for i in range(0,len(content)):
			y.append(int(content[i]))
	data = {}
	for i in range(0,len(X)):
		if y[i] in data : 
			data[y[i]].append(X[i]) 
		else :
			data[y[i]] = [X[i]]
	for i in range(1,CONST_LABELS+1):
		shuffle(data[i])

	train_X=[]
	test_y=[]
	train_y=[]
	test_X=[]

	for i in range(1,CONST_LABELS+1):
		for j in range(0,CONST_NUMBER_TRAIN_IMG/CONST_LABELS):
			train_X = train_X + [data[i][j]]
			train_y = train_y + [i]
		for j in range(CONST_NUMBER_TRAIN_IMG/CONST_LABELS, (CONST_NUMBER_TRAIN_IMG+CONST_NUMBER_TEST_IMG)/CONST_LABELS):
			test_X = test_X + [data[i][j]]
			test_y = test_y + [i]

	train_X, train_y = double_shuffle(train_X, train_y)
	test_X, test_y = double_shuffle(test_X, test_y)
 
train_X, train_y, test_X, test_y = get_data()
for c in CONST_C:
	for knl in CONST_KERNEL:
		print "Training for Kernel : ", knl, " with C : ",CONST_C 
		true_predict=0
		false_predict=0
		confidence=[]
		for j in range(1,CONST_LABELS+1):
			print "		Training One vs rest for label :", j
			X_extract=[]
			y_extract=[]
			for l in range(0,len(train_X)):
				if train_y[l]==j:
					X_extract.append(train_X[l])
					y_extract.append(1)
				else:
					X_extract.append(train_X[l])
					y_extract.append(-1)
			classifier=SVC(C=c,kernel=knl)
			classifier.fit(X_extract, y_extract)
			confidence.append(classifier.decision_function(test_X))
	    #report result
        predictions=[]
        for j in range(0,len(test_X)):
			predictions.append(-1)
			score=-999999
			for k in range(0,len(labels)):
				if confidence[k][j]>score:
					predictions[j]=labels[k]
					score=confidence[k][j]
        for j in range(0,len(predictions)):
			if predictions[j]!=test_y[j]:
				false_predict+=1
			else:
				true_predict+=1
        accuracy=(true_predict)*1.0/(true_predict+false_predict)
        print ('Accuracy = %f'%accuracy)

# def trim (a,size):
# 	return a[0:size]

# def get_train_test(X,y):
# 	train_X=[]
# 	test_y=[]
# 	train_y=[]
# 	test_X=[]
# 	indices=[0]
# 	si=1
# 	labels = []

# 	for j in range(0,len(y)):
# 		if y[j]!=si:
# 			si+=1
# 			indices.append(j-1)
# 			indices.append(j)
# 	indices.append(len(y)-1)

# 	for i in range(1,CONST_LABELS+1):
# 		labels.append(i)

# 	for i in range(0,2*CONST_LABELS,2):
# 		length=indices[i+1]-indices[i]+1
# 		for j in range(indices[i],indices[i]+length*9/10+1):
# 			train_X.append(X[j])
# 			train_y.append(y[j])
# 		for j in range(indices[i]+length*9/10+1,indices[i+1]):
# 			test_X.append(X[j])
# 			test_y.append(y[j])
# 	return train_X, train_y, test_X, test_y


# def get_data():
# 	with open(CONST_X_FILE,'r') as f:
# 		content = f.readlines()
# 		X = []
# 		for i in range(0,len(content)):
# 			X.append([float(n) for n in content[i].split()])

# 	with open(CONST_y_FILE,'r') as f:
# 		content = f.readlines()
# 		y = []
# 		for i in range(0,len(content)):
# 			y.append(int(content[i]))

# 	train_X, train_y, test_X, test_y = get_train_test(X,y)
# 	train_X,train_y = double_shuffle(train_X,train_y)
# 	test_X,test_y = double_shuffle(test_X,test_y)
# 	if CONST_TRIM: 
# 		train_X = trim(train_X,CONST_NUMBER_TRAIN_IMG)
# 		train_y = trim(train_y,CONST_NUMBER_TRAIN_IMG)
# 		test_X  = trim(test_X,CONST_NUMBER_TEST_IMG)
# 		test_y  = trim(test_y,CONST_NUMBER_TEST_IMG)
# 	return train_X, train_y, test_X, test_y
