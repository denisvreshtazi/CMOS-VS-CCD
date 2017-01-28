import csv
import os
import cv2
import numpy as np


g = input("File to open: ")
DIR = input("Directory to save : ")
f = open(g)
csv_f = csv.reader(f)

for row in csv_f:
    if row[4] == 'CCD':
        img = np.load(row[3])
            #img = cv2.imread(row[3], 0)
        x = os.path.join(DIR, 'X', 'CCD', row[1])
        if not os.path.exists(x):
            os.makedirs(x)
        imgx = cv2.Sobel(img, cv2.CV_16S, 1, 0, ksize=5)
        pathx = os.path.join(x, row[2])
            #cv2.imwrite(pathx,imgx)
        np.save(pathx, imgx)
        y = os.path.join(DIR, 'Y', 'CCD', row[1])
        if not os.path.exists(y):
            os.makedirs(y)
        imgy = cv2.Sobel(img, cv2.CV_16S, 0, 1, ksize=5)
        pathy = os.path.join(y, row[2])
            #cv2.imwrite(pathy,imgy)
        np.save(pathy, imgy)
    elif row[4] == 'CMOS':
        img = np.load(row[3])
            #img = cv2.imread(row[3], 0)
        x = os.path.join(DIR, 'X', 'CMOS', row[1])
        if not os.path.exists(x):
            os.makedirs(x)
        imgx = cv2.Sobel(img, cv2.CV_16S, 1, 0, ksize=5)
        pathx = os.path.join(x, row[2])
            #cv2.imwrite(pathx,imgx)
        np.save(pathx, imgx)
        y = os.path.join(DIR, 'Y', 'CMOS', row[1])
        if not os.path.exists(y):
            os.makedirs(y)
        imgy = cv2.Sobel(img, cv2.CV_16S, 0, 1, ksize=5)
        pathy = os.path.join(y, row[2])
            #cv2.imwrite(pathy,imgy)
        np.save(pathy, imgy)

