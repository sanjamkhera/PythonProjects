import os
import numpy as np
import matplotlib.pyplot as plt

path = "C:/Users/sanja/OneDrive - University of Manitoba/School/COMP 1012/Assignment 4"

# Used a for loop to give the user an option to view all files in the folder
listOfFiles = os.listdir(path)
for files in listOfFiles:
    print(files)

chosenFile = input("choose you would like to open:")
data = open("A4Part1TestData.txt", encoding = "UTF = 8")
list1 = []

# Used a for loop to extract X,Y values from the file and stored it in list1 
for points in data:
    points = data.readlines()
    # print(points)
    for line in points:
        point = line.split(",")
        xCoordinate = float(point[0])
        # print(xCoordinate)
        yCoordinate = float(point[1])
        # print(yCoordinate)
        dataPoint = [xCoordinate,yCoordinate]
        # print(dataPoint)
        list1.append(dataPoint)  

# Stored all X and Y Values from file to data points
dataPoints = np.array(list1)
# print(dataPoints)

X = dataPoints[:,0]
XMean = X.mean()
# print(XMean)

Y = dataPoints[:,1]
YMean = Y.mean()
# print(YMean)

XY = X*Y
XYMean = XY.mean()
# print(XYMean)

lenOfDataPoints = len(dataPoints) 
# print(lenOfDataPoints)

summationTop = 0
summationBottom = 0

# Used a for loop for least square method
for i in range(lenOfDataPoints):
    top = ((X[i]-XMean)*(Y[i]-YMean))
    summationTop = top + summationTop
    bottom = ((X[i]-XMean)**2)
    summationBottom = bottom + summationBottom

# Finding m & b Values
m = summationTop/summationBottom
b = YMean - (m*(XMean))

print("m: {} and b: {}:".format(m,b))
print()

print("The Equation of the line is: Y = {} * x + {}".format(m,b))

#plotPoints
plt.scatter(X,Y,c="b")

#PlotLine
xValues = np.arrange(1,20)

yValues = m*xValues + b

plt.plot(xValues,yValues,c="g")