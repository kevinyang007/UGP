#!/bin/bash
rm -r model
mkdir model
python svm-ovr.py
python gen-mkl-classifiers.py 
python get-ovr-results.py 