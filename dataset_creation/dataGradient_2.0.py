import pandas as pd
import csv
import os

DIR = input("Directory to read : ")
img = []
directory = []
sensor = []
camera = []

for filename in os.listdir(os.path.join(DIR, 'X', 'CCD')):
    for file in os.listdir(os.path.join(DIR, 'X', 'CCD', filename)):
        path = os.path.join(DIR, 'X', 'CCD', filename,file)
        root, ext = os.path.splitext(file)
        img += [root]
        camera += [filename]
        directory += [path]
        sensor += ["CCD"]
for filename in os.listdir(os.path.join(DIR, 'Y', 'CCD')):
    for file in os.listdir(os.path.join(DIR, 'Y', 'CCD', filename)):
        path = os.path.join(DIR, 'Y', 'CCD', filename, file)
        root, ext = os.path.splitext(file)
        img += [root]
        camera += [filename]
        directory += [path]
        sensor += ["CCD"]


a = {'Name': img, 'Camera': camera, 'PathGradient': directory, 'Sensor': sensor}
A= pd.DataFrame(a)

img1 = []
directory1 = []
sensor1 = []
camera1 = []

for filename in os.listdir(os.path.join(DIR, 'X', 'CMOS')):
    for file in os.listdir(os.path.join(DIR, 'X', 'CMOS', filename)):
        path = os.path.join(DIR, 'X', 'CMOS', filename, file)
        root, ext = os.path.splitext(file)
        camera1 += [filename]
        img1 += [root]
        directory1 += [path]
        sensor1 += ["CMOS"]
for filename in os.listdir(os.path.join(DIR, 'Y', 'CMOS')):
    for file in os.listdir(os.path.join(DIR, 'Y', 'CMOS', filename)):
        path = os.path.join(DIR, 'Y', 'CMOS', filename,file)
        root, ext = os.path.splitext(file)
        camera1 += [filename]
        img1 += [root]
        directory1 += [path]
        sensor1 += ["CMOS"]

b = {'Name': img1, 'Camera': camera1, 'PathGradient': directory1, 'Sensor': sensor1}
B = pd.DataFrame(b)

data = pd.concat([A,B], ignore_index=True)

path = input("Directory to save: ")
data.to_csv(path+'dataGradient.csv')