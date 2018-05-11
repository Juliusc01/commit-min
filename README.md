# Commit-min [![Build Status](https://travis-ci.org/Juliusc01/commit-min.svg?branch=master)](https://travis-ci.org/Juliusc01/commit-min)

Commit-min is a tool that automatically minimizes bug fix commits.

## Requirements
We have only worked from the CSE VM, but you may be able to use other systems
- Perl >= 5.0.10
- Perl Modules: Time::HiRes and IPC::Run
	- To install, run:
		```
		cpan App:cpanminus
		sudo cpanm IPC::Run
		```
- Python 2.7

## Getting started
**Setting up commit-min on your repo**

 1. Clone commit-min
	 - ```git clone https://github.com/Juliusc01/commit-min```
 2. Install commit-min on your repo
	 - ```./commit-min-install /Full/Path/To/My/Repo/```

## Example
Here is an example usage that you can follow along with by cloning this repo and running the install script from the commit-min repo:
```
git clone https://github.com/jaleum/hellogitworld
```
 1. Make some change to hellogitworld and commit
 	```
	cd hellogitworld
	echo "//this is a comment" >> src/main/java/com/github/App.java
	echo "//this is a second comment" >> src/main/java/com/github/App.java
	echo "this is a third comment" >> src/main/java/com/github/test.txt
	git add .
	git commit -m "This is a test commit"
	```
2. When prompted by commit-min, type "y" to continue
3. Input the test you want commit-min to run on
	- ``` AppTest#testApp```

Commit-min will run on this test, and output the minimized file with respect to the test, getting rid of any unnecessary lines.

The minimized file is now in place of the previous file that the test ran on, and the .bak file is the old one. NOTE that this does not yet commit for you, but it gives the minimized file ready to be committed!

## Running our tests
To run our tests, cd to commit-min and run: 
```
./runtests
```
## Evaluation
Instructions for how to run the experiments are located in the experiments directory in the Readme.txt file

## User manual
Our user manual is located at the top level of the repository, called User Manual.pdf
