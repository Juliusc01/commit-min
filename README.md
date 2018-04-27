Welcome to commit-min!

Our user manual is located at the top level of the repository, called User Manual.pdf
Travis CI info here: https://travis-ci.org/Juliusc01/commit-min/builds

Instructions to run:

First, download the repository by running:
git clone https://github.com/Juliusc01/commit-min

If you want a test repo to try this on:
git clone https://github.com/jaleum/hellogitworld.git

Then, to install our program, go into the commit-min directory (cd commit-min) and run:
./commit-min-install /Full/Path/To/My/Repo/
If you are using the test repo:
./commit-min-install /ReplaceWithYourPath/hellogitworld/

To run our program, make some changes in the git repo, run git add, and try to commit:
(First make sure you are in the repo, if you are using our test repo run :cd .. ; cd hellogitworld/)
For example, in our test repo:
echo "hi" >> README.txt
git add .
git commit -m "This is a test commit"

Now, when you try to commit, our script will be run.
Type "y" to continue, then type the name of a test you want to run our program against.
For the test repo, try 
AppTest#testApp

commit-min will run on this test, and:

INSERT END BEHAVIOR HERE
