#!/bin/bash
python mlt_get_caffe_img.py
cd ../../caffe/examples/
python feat_try.py -i ~/UGP/shubham/100_X.txt  -o ~/UGP/shubham/100_feat.txt
cd ../../UGP/shubham
python mlt_caffe_start.py
cd ../spg-gmkl