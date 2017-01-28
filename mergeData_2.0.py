import pandas as pd
import csv

data_path = input("Directory of file data : ")
d = open(data_path)
data = csv.reader(d)

grey_path = input("Directory of file data_Grey : ")
g = open(grey_path)
grey = csv.reader(g)

gradient_path = input("Directory of file data_Gradient : ")
gr = open(gradient_path)
gradient = csv.reader(gr)

result1 = pd.merge(data,grey, on=['Camera', 'Name', 'Sensor'])
final = pd.merge(result1, gradient, on=['Camera', 'Name', 'Sensor'])

path = input("Directory to save: ")
data.to_csv(path + 'Full_Data.csv')
