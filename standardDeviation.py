import csv

import math

with open("data.csv" , newline = '') as f:
    reader = csv.reader(f)
    fileData = list ( reader )

data = fileData[0]

def findMean(data):
    total = 0
    numberOfEntries = len(data)

    for i in data:
        total += int(i)

    mean = total / numberOfEntries

    return mean

squaredList = []

for item in data:
    a = int(item) - findMean(data)
    a = a ** 2
    squaredList.append(a)

sum = 0

for item in squaredList:
    sum+=item

result = sum / ( len(data) - 1 )

standardDeviation = math.sqrt(result)

print(standardDeviation)