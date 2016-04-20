with open('100_feat.txt','r') as f:
    content = f.readlines()

X = []
for i in range(0,len(content)):
    X.append([float(n) for n in content[i].split()])

with open('100_y.txt','r') as f:
    content = f.readlines()

y = []
for i in range(0,len(content)):
    y.append(int(content[i]))

with open('../spg-gmkl/mkl_input','wb') as f:
    for i in range(0,len(X)):
        f.write(str(y[i]) + " ")
        for j in range(0,len(X[0])):
            f.write(str(j+1)+":"+str(X[i][j])+" ")
        f.write("\n")    