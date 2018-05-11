In order to get the data points you have to do the following.
Setup defects4j as described here (Make sure to get your path set correctly, and source ~/.bash_profile if needed):

https://github.com/rjust/defects4j

Then, clone this repository:
git clone https://github.com/Juliusc01/commit-min

Go into the repository:
cd commit-min

And run ./evaluate 1 (Note this takes a long time)



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
containing on the first line the name of the text file of our tool's diff output
on the second line the name of the text file of the expected diff output
on the 3rd line the size of the commit
on the 4th line the number of seconds it took for our tool to run
(note: Do not include any blank lines anywhere - it will break everything)

example:
ourDiff1
expDiff1
20
120

output:
produces
precisionGraph.html
accuracyGraph.html
timeGraph.html
precisionTable.html
accuracyTable.html
timeTable.html
