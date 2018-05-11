#!/user/bin/python
import plotly
from plotly.graph_objs import Scatter, Layout, Table
import plotly.plotly as py
import plotly.graph_objs as go


def main():

    allFiles = open("diffFiles")

    fileList = allFiles.read().splitlines()

    if(len(fileList) % 2 != 0):
        print("diffFiles must be even")
        return
    i = 0
    accsList = []
    precsList = []
    comList = []
    while i < len(fileList) - 2 :
        ourFile = open(fileList[i])
        expFile = open(fileList[i+1])
        rawOurOutput = ourFile.read().splitlines()
        outSet = set(rawOurOutput)

        rawExpOutput = expFile.read().splitlines()
        expSet = set(rawExpOutput)

        accSet = expSet - outSet
        precSet = outSet - expSet

        accuracy = (len(expSet) - len(accSet)) / (len(expSet))
        precision = (len(outSet) - len(precSet)) / (len(outSet))

        accsList.append(accuracy)
        precsList.append(precision)
        comList.append(fileList[i+2])
        i+= 3

    plotly.offline.plot({
       "data": [Scatter
            (x=comList, y=accsList)],
        "layout": Layout(title="Accuracy Graph",
                          xaxis=dict(title='commit size'),
                          yaxis=dict(title='accuracy', range=[0,1.05]))
    },filename='accuracyGraph.html', auto_open=False)

    plotly.offline.plot({
        "data": [Scatter
                 (x=comList, y=precsList)],
        "layout": Layout(title="Precision Graph",
                         xaxis=dict(title='commit size'),
                         yaxis=dict(title='precision', range=[0, 1.05]))
    },filename='precisionGraph.html', auto_open=False)



    plotly.offline.plot({
        "data": [Table( header=dict(values=['Commit size', 'percent of bug fix lines found']),
    cells=dict(values=[comList,
                       accsList]))],
        "layout": Layout(title="commit size vs accuracy")
    })

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

if __name__ == '__main__':
    main()