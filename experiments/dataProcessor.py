#!/user/bin/python
import plotly
from plotly.graph_objs import Scatter, Layout, Table, Bar
import plotly.offline as py
import plotly.graph_objs as go

'''
Produces a graphs and tables based on the tools diff and expected diff
given in the diffFiles file. Produces a accuracy, precision, and
time bar graph and Table. For more information about what those are
look in readme.
'''
def main():

    allFiles = open("diffFiles.txt")

    fileList = allFiles.read().splitlines()

    if(len(fileList) % 4 != 0):
        print("diffFiles must be multiple of four")
        return
    i = 0
    accsList = []
    precsList = []
    timeList = []
    comList = []
    while i < len(fileList) - 3 :
        ourFile = open(fileList[i])
        expFile = open(fileList[i+1])
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


    #producing bar graphs for accuracy, precision, and time
    plotly.offline.plot({
       "data": [Bar
            (x=comList, y=accsList, width=1)],
        "layout": Layout(title="Bug number vs Accuracy Graph",
                        xaxis=dict(title='Bug number'),
                        yaxis=dict(title='percent of bug fix lines found', range=[0,1.05])

                        )
    },filename='accuracyGraph.png', auto_open=False)

    plotly.offline.plot({
        "data": [Bar
                 (x=comList, y=precsList, width=1)],
        "layout": Layout(title="Bug number vs Precision Graph",
                         xaxis=dict(title='Bug number'),
                         yaxis=dict(title='percent of tools bug fix lines valid(valid means line in expected)', range=[0, 1.05]))
    },filename='precisionGraph.png', auto_open=False)

    plotly.offline.plot({
        "data": [Bar
                 (x=comList, y=timeList, width=1)],
        "layout": Layout(title="Bug number vs Time Graph",
                         xaxis=dict(title='Bug number'),
                         yaxis=dict(title='time for tool to run(seconds)'))
    }, filename='timeGraph.png', auto_open=False)


    #producing tables for accuracy, precision, and time
    plotly.offline.plot({
        "data": [Table( header=dict(values=['Bug number', 'percent of bug fix lines found']),
    cells=dict(values=[comList,
                       accsList]))],
        "layout": Layout(title="Bug number vs accuracy")
    },filename='accuracyTable.png', auto_open=False)

    plotly.offline.plot({
        "data": [Table(header=dict(values=['Bug number', 'percent of tools bug fix lines valid(valid means line in expected)']),
                       cells=dict(values=[comList,
                                          precsList]))],
        "layout": Layout(title="Bug number vs precision")
    }, filename='precisionTable.png', auto_open=False)

    plotly.offline.plot({
        "data": [Table(
            header=dict(values=['Bug number', 'time for tool to run(seconds)']),
            cells=dict(values=[comList,
                               timeList]))],
        "layout": Layout(title="Bug number vs Time Graph")
    }, filename='timeTable.png', auto_open=False)



if __name__ == '__main__':
    main()
