import pandas as pd
import csv
import os
img =[]
directory = []
sensor = []
camera = []
DIR = input("Directory to read : ")

for filename in os.listdir(DIR+'\CCD'):
    for file in os.listdir(os.path.join(DIR+'\CCD', filename)):
        path = os.path.join(DIR+'\CCD', filename,file)
        root, ext = os.path.splitext(file)
        img +=[root]
        camera +=[filename]
        directory +=[path]
        sensor += ["CCD"]


a = {'Name': img,'Camera': camera, 'Path': directory, 'Sensor': sensor}
A= pd.DataFrame(a)
img1 =[]
directory1 = []
sensor1 = []
camera1 = []
for filename in os.listdir(DIR+'\CMOS'):
    for file in os.listdir(os.path.join(DIR+'\CMOS', filename)):
        path = os.path.join(DIR+'\CMOS', filename,file)
        camera1 += [filename]
        root, ext = os.path.splitext(file)
        img1 += [root]
        directory1 +=[path]
        sensor1 += ["CMOS"]

b = {'Name': img1,'Camera': camera1, 'Path': directory1, 'Sensor': sensor1}
B = pd.DataFrame(b)

data = pd.concat([A,B], ignore_index=True)
path = input("Directory to save: ")
data.to_csv(path+'data.csv')

