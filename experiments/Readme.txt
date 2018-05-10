To create graphs through dataProcessor must first install plotly
can be done by either
$ pip install plotly
or 
$ sudo pip install plotly

after this run
python dataProcessor.py

important:
for this to work must have
diffFiles.txt
containing on the first line the name of the text file of our tool's diff output
on the second line the name of the text file of the expected diff output
and on the 3rd line the size of the commit
example:
ourDiff1
expDiff1
20

output:
produces a
precisionGraph.html and a
accuracyGraph.html