import csv

with open('SOCR-HeightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)


newData =[]
for i in range(len(fileData)):
    num = fileData[i][1]
    newData.append(float(num))


newData.sort()

n = len(newData)


if n%2 ==0:
    num1 = float(newData[n//2])
    num2 = float(newData[n//2 -1])

    median = (num1+num2)/2

else:
    median = newData[n//2]

print(median)



