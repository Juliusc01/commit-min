import os
import sys
import linecache

def func(files):
    # files = sys.argv[1]
    #path_to_files = sys.argv[2]
    script_dir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(script_dir)
    if '.txt' not in files:
        raise Exception('Pass in a text file')

    os.system('rm -rf tmp results output_file.txt')
    os.system('mkdir tmp')
    os.system('cd tmp && mkdir new && mkdir old')

    f = open(files)
    # one file per line
    new_file_path = script_dir +"/tmp/new/"
    old_file_path = script_dir +"/tmp/old/"
    tmp_path = script_dir + "/tmp"

    # parse input
    actual_files = []
    paths = []
    for line in f:
        t = line.rpartition("/")
        repo = t[0]
        actual_files.append(t[2].rstrip('\n'))
        paths.append(t[0] + t[1])
    #copy into new folder
    for i in range(len(actual_files)):
        c = 'cp ' + paths[i] + actual_files[i] + ' ' + new_file_path
        os.system(c)

    os.chdir(repo)
    os.system('pwd')
    os.system('git stash --include-untracked')
    os.chdir(script_dir)
    # # copy into old folder
    for i in range(len(actual_files)):
        c = 'cp ' + paths[i] + actual_files[i] + ' ' + old_file_path
        os.system(c)

    # # TODO HANDLE NEWLY CREATED FILE
    os.chdir(repo)
    os.system('git stash apply')

    # Run JPlag on files individually
    os.chdir(script_dir)
    os.system('cd tmp && mkdir compare && cd compare && mkdir new && mkdir old')
    compare_path = 'tmp/compare'
    os.system('mkdir results')
    resultpath = script_dir + "/results"
    outputfile = open('/tmp/refactorfiles.txt', 'w') # /tmp/refactorfiles.txt
    full_compare = script_dir + '/tmp/compare'
    output = []
    i = 0
    for file in actual_files:
        c = 'cp tmp/new/' + file + ' ' + compare_path + '/new'
        os.system(c)
        c = 'cp tmp/old/' + file + ' ' + compare_path + '/old'
        os.system(c)
        s = "java -jar jplag-2.11.9-SNAPSHOT-jar-with-dependencies.jar -l java17 -r {0} -s {1}".format(resultpath, full_compare)
        os.system(s)
        # Check if its 100% similarity
        os.chdir('results')
        result_line = linecache.getline('index.html', 42)
        if(result_line.find('100.0') == -1):
            output.append(paths[i] + file)
        # delete all results for this comparison
        os.system('rm *')
        os.chdir(full_compare)
        os.system('cd old && rm * && cd .. && cd new && rm *')
        os.chdir(script_dir)

        i+=1

    # print modified files to output file
    for i in range(len(output)):
        if(i < len(output) -1):
            outputfile.write(output[i]+'\n')
        else:
            outputfile.write(output[i])
    outputfile.close()

    c = 'rm -rf ' + script_dir + '/results tmp'
    os.system(c)   