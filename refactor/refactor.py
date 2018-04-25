import os
import sys
import linecache
#/homes/iws/eblajev/Downloads/exercise1/eblajev/simpledb
files = sys.argv[1]
path_to_files = sys.argv[2]

cur_folder = os.getcwd()

if '.txt' not in files:
    raise Exception('Pass in a text file')

os.system('rm -rf tmp results output_file.txt')
os.system('mkdir tmp')
os.system('cd tmp && mkdir cur && mkdir old')

f = open(files)
# one line file that is comma seperated
fileList = f.readline().strip().split(',')
new_file_path = cur_folder +"/tmp/cur/"
old_file_path = cur_folder +"/tmp/old/"
tmp_path = cur_folder + "/tmp"
# copy new files into cur folder
os.chdir(path_to_files)
for file in fileList:
    c = 'cp ' + file + ' ' + new_file_path
    os.system(c)

os.system('git stash --include-untracked')
os.chdir(path_to_files)
for file in fileList:
    c = 'cp ' + file + ' ' + old_file_path
    os.system(c)
# HANDLE NEWLY CREATED FILE
os.system('git stash apply')

# Run JPlag on files individually
os.chdir(cur_folder)
os.system('mkdir results')
resultpath = cur_folder + "/results"
outputfile = open('output_file.txt', 'w')
output = []
for file in fileList:
    s = "java -jar jplag-2.11.9-SNAPSHOT-jar-with-dependencies.jar -l java17 -r {0} -s {1}".format(resultpath, tmp_path)
    os.system(s)
    # Check if its 100% similarity
    os.chdir('results')
    result_line = linecache.getline('index.html', 42)
    if(result_line.find('100.0') == -1):
        output.append(file)
    # delete all results for this comparison
    os.system('rm *')

# print modified files to output file
for i in range(len(output)):
    if(i < len(output) -1):
        outputfile.write(output[i]+'\n')
    else:
        outputfile.write(output[i])
outputfile.close()

