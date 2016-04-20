import os
rootdir = '../Datasets/Caltech/101_ObjectCategories'
out_img = open('100_X.txt','wb')
out_label = open('100_y.txt','wb')
j = 0
k = 0 
for dirpath, dirnames, filenames in os.walk(rootdir):
    i = 0
    #k+=1
    #if k < 10 :
    #    continue
    for file in filenames:
        file= os.path.join(os.path.abspath(dirpath), file)
        label = os.path.basename(os.path.normpath(os.path.abspath(dirpath)))
        out_img.write(file+'\n')
        out_label.write(str(j)+'\n')
    #    i=i+1
    #    if(i>30):
    #        break
    #if j>0 :
    #    break 
    j += 1
