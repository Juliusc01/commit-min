#!/user/bin/python
import plotly
from plotly.graph_objs import Scatter, Layout, Table, Bar
import plotly.offline as py
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

    '''
    trace1 = go.Bar(
        x=['giraffes', 'orangutans', 'monkeys'],
        y=[20, 14, 23],
        name='SF Zoo'
    )
    trace2 = go.Bar(
        x=['giraffes', 'orangutans', 'monkeys'],
        y=[12, 18, 29],
        name='LA Zoo'
    )

    data = [trace1, trace2]
    layout = go.Layout(
        barmode='group'
    )

    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='grouped-bar')
    '''
    plotly.offline.plot({
       "data": [Bar
            (x=comList, y=accsList, width=1)],
        "layout": Layout(title="Bug number vs Accuracy Graph",
                        xaxis=dict(title='Bug number'),
                        yaxis=dict(title='percent of bug fix lines found', range=[0,1.05])

                        )
    },filename='accuracyGraph.html', auto_open=False)

    plotly.offline.plot({
        "data": [Bar
                 (x=comList, y=precsList, width=1)],
        "layout": Layout(title="Bug number vs Precision Graph",
                         xaxis=dict(title='Bug number'),
                         yaxis=dict(title='percent of tools bug fix lines valid(valid means line in expected)', range=[0, 1.05]))
    },filename='precisionGraph.html', auto_open=False)

    plotly.offline.plot({
        "data": [Bar
                 (x=comList, y=timeList, width=1)],
        "layout": Layout(title="Bug number vs Time Graph",
                         xaxis=dict(title='Bug number'),
                         yaxis=dict(title='time for tool to run(seconds)'))
    }, filename='timeGraph.html', auto_open=False)



    plotly.offline.plot({
        "data": [Table( header=dict(values=['Bug number', 'percent of bug fix lines found']),
    cells=dict(values=[comList,
                       accsList]))],
        "layout": Layout(title="Bug number vs accuracy")
    },filename='accuracyTable.html', auto_open=False)

    plotly.offline.plot({
        "data": [Table(header=dict(values=['Bug number', 'percent of tools bug fix lines valid(valid means line in expected)']),
                       cells=dict(values=[comList,
                                          precsList]))],
        "layout": Layout(title="Bug number vs precision")
    }, filename='precisionTable.html', auto_open=False)

    plotly.offline.plot({
        "data": [Table(
            header=dict(values=['Bug number', 'time for tool to run(seconds)']),
            cells=dict(values=[comList,
                               timeList]))],
        "layout": Layout(title="Bug number vs Time Graph")
    }, filename='timeTable.html', auto_open=False)

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