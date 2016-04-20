import os
import random
from sklearn.externals import joblib
random.seed(10)
CONST_s = "_all"
CONST_labels = 102
CONST_X = "../shubham/100_feat.txt"
CONST_y = "../shubham/100_y.txt"
CONST_USE_ENTIRE_DATA = 1 
CONST_NUMBER_TRAIN_IMG = 350 
CONST_NUMBER_TEST_IMG = 150 
CONST_DATA_DUMP = 'model'+CONST_s'/dump'

def double_shuffle(a,b):
    an = []
    bn = []
    index = []
    for i in range(0,len(a)):
        index.append(i) 
    random.shuffle(index)
    for i in range(0,len(index)):   
        an.append(a[index[i]])
        bn.append(b[index[i]])
    return an,bn

def trim_data(data):
	train_X=[]
	test_y=[]
	train_y=[]
	test_X=[]
	if CONST_USE_ENTIRE_DATA == 1:
		for i in range(1,CONST_labels+1):
			for j in range(0,int(len(data[i])*0.9)):
				train_X = train_X + [data[i][j]]
				train_y = train_y + [i]
			for j in range(int(len(data[i])*0.9), len(data[i])):
				test_X = test_X + [data[i][j]]
				test_y = test_y + [i]
	else : 
		print('Trimming Data Set Train : ',CONST_NUMBER_TRAIN_IMG,', Test : ',CONST_NUMBER_TEST_IMG)
		for i in range(1,CONST_labels+1):
			for j in range(0,CONST_NUMBER_TRAIN_IMG/CONST_labels):
				try : 
					train_X = train_X + [data[i][j]]
					train_y = train_y + [i]
				except Exception as e:
					print 'Insufficient Train Images for label : ', j
					break
			for j in range(CONST_NUMBER_TRAIN_IMG/CONST_labels, (CONST_NUMBER_TRAIN_IMG+CONST_NUMBER_TEST_IMG)/CONST_labels):
				try:	
					test_X = test_X + [data[i][j]]
					test_y = test_y + [i]
				except Exception as e:
					print 'Insufficient Test Images for label : ', j
					break
	return train_X, train_y, test_X, test_y

def get_binary_data(y,pos_label):
	binary_y = []
	for i in range(0,len(y)):
		if y[i] == pos_label:
			binary_y.append(1)
		else:
			binary_y.append(-1)
	return binary_y

def write_mkl_input(X, y,filename):
	with open(filename,'wb') as f:
		content = ""
		for i in range(0,len(X)):
			content += str(y[i]) + " "
			for j in range(0,len(X[i])):
				content += str(j+1)+":"+str(X[i][j])+" "
			content += "\n"
		f.write(content)

def prepare_data(train_X, train_y, test_X, test_y):
	if not os.path.exists("model"+CONST_s):
		os.makedirs("model"+CONST_s)
	for i in range(1,CONST_labels+1):
		print "Writing Data for label "+str(i)
		binary_train_y = []
		binary_test_y = []
		if not os.path.exists("model"+CONST_s+"/"+str(i)):
			os.makedirs("model"+CONST_s+"/"+str(i))
		binary_train_y = get_binary_data(train_y, i)
		binary_test_y = get_binary_data(test_y, i)
		write_mkl_input(train_X, binary_train_y, "model"+CONST_s+"/"+str(i)+"/mkl_train")
		write_mkl_input(test_X, binary_test_y, "model"+CONST_s+"/"+str(i)+"/mkl_test")

def load_data():
	with open(CONST_X,'r') as f:
	    content = f.readlines()
	X = []
	for i in range(0,len(content)):
	    X.append([float(n) for n in content[i].split()])

	with open(CONST_y,'r') as f:
	    content = f.readlines()
	y = []
	for i in range(0,len(content)):
	    y.append(int(content[i]))
	return X,y

def get_data():
	X,y = load_data()
	data = {}
	for i in range(0,len(X)):
		if y[i] in data : 
			data[y[i]].append(X[i]) 
		else :
			data[y[i]] = [X[i]]
	for i in range(1,CONST_labels+1):
		random.shuffle(data[i])

	train_X, train_y, test_X, test_y = trim_data(data)
	train_X, train_y = double_shuffle(train_X, train_y)
	test_X, test_y = double_shuffle(test_X, test_y)
	dump = {}
	dump['train_X'] = train_X
	dump['train_y'] = train_y
	dump['test_X'] = test_X
	dump['test_y'] = test_y 
	if not os.path.exists("model"+CONST_s):
		os.makedirs("model"+CONST_s)
	joblib.dump(dump,CONST_DATA_DUMP)
	return train_X, train_y, test_X, test_y

train_X, train_y, test_X, test_y = get_data()
prepare_data(train_X, train_y, test_X, test_y)