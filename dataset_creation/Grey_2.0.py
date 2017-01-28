
import csv
import os
from PIL import Image
import numpy as np

g = input("File to open: ")
DIR = input("Directory to save : ")
f = open(g)
csv_f = csv.reader(f)

for row in csv_f:
    if row[4] == 'CCD':
        img = np.asarray(Image.open(row[3]).convert('L'))
        p = os.path.join(DIR, 'CCD', row[1])
        if not os.path.exists(p):
            os.makedirs(p)
        path = os.path.join(p, row[2])
        np.save(path, img)
    elif row[4] == 'CMOS':
        img = Image.open(row[3]).convert('L')
        p = os.path.join(DIR, 'CMOS', row[1])
        if not os.path.exists(p):
            os.makedirs(p)
        path = os.path.join(p, row[2])
        np.save(path, img)
