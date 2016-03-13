import cv2
import json
from pprint import pprint
import os

# For modification of cordinates 
def getCordinates(height, width, x, y, w, h):
    if x < 0:
        x = 0
    if y < 0:
        y = 0
    if x > width:
        x = width 
    if y > height:
        y = height 
    return x,y,w,h

with open('labels.json') as data_file:    
    data = json.load(data_file)

for i in range(0,len(data)):
    imagename = data[i]['filename']
    img = cv2.imread(imagename)
    height,width = img.shape[:2] 
    for j in range(0,len(data[i]['annotations'])):
        cls = data[i]['annotations'][j]['class']
        if cls == 'initialized':
            continue
        x = data[i]['annotations'][j]['x']
        y = data[i]['annotations'][j]['y']
        w = data[i]['annotations'][j]['width']
        h = data[i]['annotations'][j]['height']
        x,y,w,h = getCordinates(height, width, x, y, w, h)
        crop_img = img[y:y+h,x:x+w] 
        #cv2.imshow("cropped", crop_img)
        #cv2.waitKey(0)
        croppend_img_name = 'dataset/' + cls + '/' + os.path.splitext(os.path.basename('dataset/'+cls+'/'+imagename ))[0] + '_'+str(j)+'.bmp'
        if not cv2.imwrite(croppend_img_name, crop_img): 
            print 'Unable to save ', croppend_img_name


