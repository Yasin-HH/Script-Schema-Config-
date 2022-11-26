import pandas
import csv

data = pandas.read_csv('CSV/Machine_Adresse.csv')
data1 = pandas.read_csv('CSV/Machine_Adresse.csv')
data2 = pandas.read_csv('CSV/Machine_Name.csv')
data3 = pandas.read_csv('CSV/Machine_Types.csv')


m = pandas.merge(data,data1)
n = pandas.merge(data2,data3)
print(n)
print(m)
a = pandas.merge(n,m)

#print (a)


print(a)