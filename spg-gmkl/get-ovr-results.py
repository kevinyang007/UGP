import os
from sklearn.externals import joblib
import sys

CONST_s = "_all"
CONST_labels = 102
CONST_X = "../shubham/100_feat.txt"
CONST_y = "../shubham/100_y.txt"
CONST_USE_ENTIRE_DATA = 1 
CONST_NUMBER_TRAIN_IMG =  35
CONST_NUMBER_TEST_IMG = 10 
CONST_DATA_DUMP = 'model'+CONST_s+'/dump'

def load_prediction(file):
	with open(file,'r') as f:
	    content = f.readlines()
	X = { 'list' : []}  
	content[0].rstrip("\n")
	print content[0]
	if content[0] == 'labels 1 -1\n' :
		X['column'] = 1 
	elif content[0] == 'labels -1 1\n':
		X['column'] = 2 
	else :
		print "ERROR"
		sys.exit()
	for i in range(1,len(content)):
		content[i].rstrip("\n")
		X['list'].append([float(n) for n in content[i].split()])
	return X

def get_max_index(scores) : 
	index = 0
	for i in range(0,len(scores)):
		if scores[i] > scores[index]:
			index = i 
	print "Max Score ", scores[index]
	return index+1

def get_ovr_prediction(predictions):
	ovr = []
	for j in range(0,len(predictions[1]['list'])):
		scores = []
		for i in range(1,CONST_labels+1):
			column = predictions[i]['column']
			scores.append(predictions[i]['list'][j][column])
		k = get_max_index(scores)
		ovr.append(k)
	return ovr

def get_results(predicted, test_y):
	correct = 0
	for i in range(0,len(test_y)):
		print predicted[i], test_y[i]
		if predicted[i] == test_y[i]:
			correct+=1
	print "correct = " , correct
	print "Accuracy = ", correct*100.0/len(test_y)

data = joblib.load(CONST_DATA_DUMP)
predictions = {} 
for i in range(1,CONST_labels+1):
	base = "model"+CONST_s+"/"+str(i)+"/"
	prediction_file = base + "prediction"
	predictions[i] = load_prediction(prediction_file)

predicted = get_ovr_prediction(predictions)
get_results(predicted, data['test_y'])