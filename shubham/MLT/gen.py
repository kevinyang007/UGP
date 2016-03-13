import os
from os import listdir
from os.path import isfile, join, dirname
mypath = os.getcwd() + '/images'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
onlyfies = sorted(onlyfiles)
f = open(os.getcwd()+'/labels.json', 'ab')
f.write('[\n')
for i in xrange(len(onlyfiles)):
    onlyfiles[i] = 'images/'+onlyfiles[i]
    f.write('{\n')
    f.write('"class":"image",\n')
    f.write('"filename":"'+onlyfiles[i]+'",\n')
    f.write('"annotations": [\n{\n"class": "initialized",\n"height": 75.0,\n"type":"rect",\n"width": 40.0,\n"y": 105.0,\n"x": 346.0\n}\n]\n}')
    if i != len(onlyfiles)-1:
       f.write(',\n') 
f.write(']')
