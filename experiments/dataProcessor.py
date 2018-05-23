#!/user/bin/python
import plotly
from plotly.graph_objs import Scatter, Layout, Table
import plotly.plotly as py
import plotly.graph_objs as go
import os
import sys
import signal


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    allFiles = open(dir_path+"/diffFiles.txt")

    fileList = allFiles.read().splitlines()

    if(len(fileList) % 2 != 0):
        print("diffFiles must be even")
        return
    i = 0
    accsList = []
    precsList = []
    timeList = []
    comList = []
    while i < len(fileList) - 3 :
        ourFile = open(dir_path+"/"+fileList[i])
        expFile = open(dir_path+"/"+fileList[i+1])
        rawOurOutput = ourFile.read().splitlines()
        outSet = set(rawOurOutput)

        rawExpOutput = expFile.read().splitlines()
        expSet = set(rawExpOutput)

        accSet = expSet - outSet
        precSet = outSet - expSet

        accuracy = float(len(expSet) - len(accSet)) / float(len(expSet))
        precision = float(len(outSet) - len(precSet)) / float(len(outSet))

        accsList.append(accuracy)
        precsList.append(precision)
        comList.append(fileList[i+2])
        timeList.append(fileList[i+3])
        i += 4

    plotly.offline.plot({
       "data": [Scatter
            (x=comList, y=accsList)],
        "layout": Layout(title="Bug number vs Accuracy Graph for " + sys.argv[1],
                          xaxis=dict(title='Bug number'),
                          yaxis=dict(title='percent of bug fix lines found', range=[0,1.05]))
    },filename='accuracyGraph' + sys.argv[1] + '.html', auto_open=False)

    plotly.offline.plot({
        "data": [Scatter
                 (x=comList, y=precsList)],
        "layout": Layout(title="Bug number vs Precision Graph for " + sys.argv[1],
                         xaxis=dict(title='Bug number'),
                         yaxis=dict(title='percent of tools bug fix lines valid(valid means line in expected)', range=[0, 1.05]))
    },filename='precisionGraph' + sys.argv[1] + '.html', auto_open=False)

    plotly.offline.plot({
        "data": [Scatter
                 (x=comList, y=timeList)],
        "layout": Layout(title="Bug number vs Time Graph for " + sys.argv[1],
                         xaxis=dict(title='Bug number'),
                         yaxis=dict(title='time for tool to run(seconds)'))
    }, filename='timeGraph' + sys.argv[1] + '.html', auto_open=False)



    plotly.offline.plot({
        "data": [Table( header=dict(values=['Bug number', 'percent of bug fix lines found']),
    cells=dict(values=[comList,
                       accsList]))],
        "layout": Layout(title="Bug number vs Accuracy for " + sys.argv[1])
    },filename='accuracyTable' + sys.argv[1] + '.html', auto_open=False)

    plotly.offline.plot({
        "data": [Table(header=dict(values=['Bug number', 'percent of tools bug fix lines valid(valid means line in expected)']),
                       cells=dict(values=[comList,
                                          precsList]))],
        "layout": Layout(title="Bug number vs Precision for " + sys.argv[1])
    }, filename='precisionTable' + sys.argv[1] + '.html', auto_open=False)

    plotly.offline.plot({
        "data": [Table(
            header=dict(values=['Bug number', 'time for tool to run(seconds)']),
            cells=dict(values=[comList,
                               timeList]))],
        "layout": Layout(title="Bug number vs Time for " + sys.argv[1])
    }, filename='timeTable' + sys.argv[1] + '.html', auto_open=False)

    #data = [accTrace]
    #py.iplot(data, filename='scatter-mode')


    #print("accuracy", accsList[1])
    #print("precision", precsList[1])

    '''
    plotly.offline.plot({
        "data": [Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
        "layout": Layout(title="hello world")
    })
    '''
def interrupt_handler():
  sys.exit(0)

if __name__ == '__main__':
  signal.signal(signal.SIGINT, interrupt_handler)
  main()
