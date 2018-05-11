Welcome to commit-min!

Instructions for how to run the experiments are located in the experiments directory in the Readme.txt file

Our user manual is located at the top level of the repository, called User Manual.pdf

Travis CI info here: https://travis-ci.org/Juliusc01/commit-min/builds

To run the tests: ./runtests

Instructions to run:

First, download the repository by running:
git clone https://github.com/Juliusc01/commit-min

If you want a test repo to try this on:
git clone https://github.com/jaleum/hellogitworld

Then, to install our program, go into the commit-min directory (cd commit-min) and run:

./commit-min-install /Full/Path/To/My/Test/Repo/
If you are using the test repo:

./commit-min-install /ReplaceWithYourPath/hellogitworld/

To run our program, make some changes in the git repo, run git add, and try to commit:
(First make sure you are in the repo, if you are using our test repo run :cd .. ; cd hellogitworld/)
For example, in our test repo:

echo "//this is a comment" >> src/main/java/com/github/App.java ; echo "//this is a second comment" >> src/main/java/com/github/App.java ; echo "this is a third comment" >> src/main/java/com/github/test.txt ; git add . ; git commit -m "This is a test commit"

Now, when you try to commit, our script will be run.
Type "y" to continue, then type the name of a test you want to run our program against.
For the test repo, try 
AppTest#testApp

Commit-min will run on this test, and output the minimized file with respect to the test, getting rid of any unnecessary lines.
The minimized file is now in place of the previous file that the test ran on, and the .bak file is the old one. NOTE that this does not yet commit for you, but it gives the minimized file ready to be committed!

The full test example (insert correct path for INSERTPATHHERE , you should just put in what you get from pwd)
note after the end of each $ line press enter
for the cpan App:cpaniminus you must enter yes and sudo before moving on:

$git clone https://github.com/Juliusc01/commit-min ; git clone https://github.com/jaleum/hellogitworld ; cd commit-min

$cpan App:cpanminus
$sudo cpanm IPC::Run


$./commit-min-install /INSERTPATHHERE/hellogitworld/ ; cd .. ; cd hellogitworld/ ; echo "//this is a comment" >> src/main/java/com/github/App.java ; echo "//this is a second comment" >> src/main/java/com/github/App.java ; echo "this is a third comment" >> src/main/java/com/github/test.txt ; git add . ; git commit -m "This is a test commit"

Type y, then type AppTest#testApp

Now, go into hellogitworld/src/main/java/com/github/
App.java is the new minimized file (note the lack of comment!), and App.java.bak is the old file (note the comment)

