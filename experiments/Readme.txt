To create graphs through dataProcessor must first install plotly
which must be done through pip which can be done by either

$ pip install plotly
or 
$ sudo pip install plotly

steps to install pip and plotly together how i personally did it
might be susceptable to malware I don't know:
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py --user
pip install plotly --user
after this run
python dataProcessor.py

important:
for this to work must have
diffFiles.txt
containing on the first line the name of the diff text file of our tool's diff output
on the second line the name of the diff text file of the expected diff output
on the 3rd line the size of the commit
on the 4th line the number of seconds it took for our tool to run
(note: Do not include any blank lines anywhere - it will break everything)

example:
ourDiff1
expDiff1
20
120

note we included dummy code to show what the graphs and tables will look like with data
to get it to work with actual data replace the dummy data with actual data in diffFiles.txt

output:
produces
precisionGraph.html
accuracyGraph.html
timeGraph.html
precisionTable.html
accuracyTable.html
timeTable.html

NOTE: The following section is how you would get our evaluation data, but 
we never let it run long enough to finish so I wouldn't recommend trying to
set it up.

In order to run our evaluation script, you must install defects4j:
https://github.com/rjust/defects4j

From the commit-min repo, run:
./evaluate 1

The 1 signifies it will evaluate one bug fix. Our evaluate script was the ability
to run on multiple projects as well as multiple bug fixes. Unfortunately, commit-min
was still trying to minimize things after 3 hours of running, so we never got real
results.

