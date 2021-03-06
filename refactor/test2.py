import os
import commands
import sys

# This tests refactor tool, should be 100% refactor

script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)

os.system('rm -rf tests')
os.system('mkdir tests && cd tests && mkdir src')
os.chdir('tests/src')
os.system('git clone https://github.com/Dilraj-Singh-Devgun/Data-Structures.git')
os.chdir('Data-Structures/src/Queues')

f = open('LinkedListBasedQueue.java', 'r')
contents = f.readlines()
f.close()

contents.insert(0, '// This new comment should be a refactor!\n')
f = open('LinkedListBasedQueue.java', 'w')
contents = "".join(contents)
f.write(contents)
f.close()

os.chdir(script_dir + '/tests/src')
s = os.getcwd()
print s
os.system('echo ' + s + "/Data-Structures/src/Queues/LinkedListBasedQueue.java > files.txt")
os.chdir(script_dir)
filedir = script_dir + '/tests/src/files.txt'
repodir = script_dir + '/tests/src/Data-Structures'
s = 'python refactor.py ' +  filedir + ' ' + repodir
os.system(s)
c = 'rm -rf ' + script_dir + '/tests'
os.system(c)

result = commands.getoutput('wc -c < output_file.txt')
if (result != '0'):
    sys.exit(-1)
