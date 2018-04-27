Welcome to commit-min!

Our user manual is located at the top level of the repository, called User Manual.pdf
Travis CI info here: https://travis-ci.org/Juliusc01/commit-min/builds

Instructions to run:

First, download the repository by running:
git clone https://github.com/Juliusc01/commit-min

If you want a test repo to try this on:
git clone https://github.com/jaleum/hellogitworld

Then, to install our program, go into the commit-min directory (cd commit-min) and run:

./commit-min-install /Full/Path/To/My/Repo/
If you are using the test repo:

./commit-min-install /ReplaceWithYourPath/hellogitworld/

To run our program, make some changes in the git repo, run git add, and try to commit:
(First make sure you are in the repo, if you are using our test repo run :cd .. ; cd hellogitworld/)
For example, in our test repo:

echo "//this is a comment" >> src/main/java/com/github/App.java ; git add . ; git commit -m "This is a test commit"

Now, when you try to commit, our script will be run.
Type "y" to continue, then type the name of a test you want to run our program against.
For the test repo, try 
AppTest#testApp

Commit-min will run on this test, and output the minimized file with respect to the test, getting rid of any unnecessary lines.
The minimized file is now in place of the previous file that the test ran on, and the .bak file is the old one. NOTE that this does not yet commit for you, but it gives the minimized file ready to be committed!

The full test example (insert correct path):
git clone https://github.com/Juliusc01/commit-min ; git clone https://github.com/jaleum/hellogitworld ; cd commit-min ; ./commit-min-install /INSERTPATHHERE/hellogitworld/ ; cd .. ; cd hellogitworld/ ; echo "//this is a comment" >> src/main/java/com/github/App.java ; git add . ; git commit -m "This is a test commit" 
Type y, then type AppTest#testApp

Now, go into hellogitworld/src/main/java/com/github/
App.java is the new minimized file (note the lack of comment!), and App.java.bak is the old file (note the comment)
