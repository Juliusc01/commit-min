import os
import commands
import refactor
import sys

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

os.system('echo "tests/src/Data-Structures/src/Queues/LinkedListBasedQueue.java" > files.txt')
os.chdir(script_dir)
refactor.func('tests/src/files.txt', 'tests/src/Data-Structures')
# s = 'python refactor.py tests/src/files.txt tests/src/Data-Structures'
# os.system(s)
c = 'rm -rf ' + script_dir + '/tests'
os.system(c)

result = commands.getoutput('wc -l < output_file.txt')
if (result != '0'):
    sys.exit(-1)

