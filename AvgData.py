import csv
import plotly.figure_factory as ff
import statistics
import pandas as pd
import random

file1 = pd.read_csv("Avg_Data.csv")
data = file1["average"].tolist()

figure = ff.create_distplot([data], ["average"], show_hist = False)
figure.show()

mean1 = statistics.mean(data)
print("The mean is ", mean1)

mode1 = statistics.mode(data)
print("The mode is ", mode1)

std_dev = statistics.stdev(data)
print("Standard Deviation is ", std_dev)

def sampleData(counter) : 
    dataSample = []
    for i in range(0,counter) : 
        rs = random.randint(0,len(data)-1)
        value = data[rs]
        dataSample.append(value)

    sMean = statistics.mean(dataSample)
    return sMean
# print("The mean of the sample data is ", sMean)

    sDev = statistics.stdev(dataSample)
    print("The standard deviation of the sample data is ", sDev)

def showGraph(mList) : 
    data2 = mList
    figure2 = ff.create_distplot([data2],["average"], show_hist=False)
    figure2.show()

def main() : 
    mList = []
    for i in range(0,1000) : 
        mSets = sampleData(100)
        mList.append(mSets)
        samplingM = statistics.mean(mList)
        print("The mean for sample data is ", samplingM)
        samplingDev = statistics.stdev(mList)
        print("The standard deviation for sample data is ", samplingDev)
    showGraph(mList)
main()