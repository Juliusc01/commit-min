import os
import commands
script_dir = os.getcwd()
os.system('rm -rf tests')
os.system('mkdir tests && cd tests && mkdir src')
os.chdir('tests/src')
os.system('git clone https://github.com/Dilraj-Singh-Devgun/Data-Structures.git')
os.chdir('Data-Structures/src/Stack')

f = open('ArrayBasedStack.java', 'r')
contents = f.readlines()
f.close()

contents.insert(0,'public void foo(){} \n')
f = open('ArrayBasedStack.java', 'w')
contents = "".join(contents)
f.write(contents)
f.close()

os.chdir(script_dir + '/tests/src')

os.system('echo "tests/src/Data-Structures/src/Stack/ArrayBasedStack.java" > files.txt')
os.chdir(script_dir)
s = 'python refactor.py tests/src/files.txt tests/src/Data-Structures'
os.system(s)

# result = commands.getoutput('wc -c output_file.txt')

# print result

#Data-Structures/src/DataStructures.java