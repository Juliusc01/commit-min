#!/usr/bin/python
import os
from rundelta import parse_diff

def main():
    print
    print "Starting parse diff test..."
    if not testParseDiff():
        print "Parse diff test failed!"
        return sys.exit()
    else:
        print "Parse diff test succeeded!"

def testParseDiff():
    script_dir = os.path.dirname(__file__)
    diff_file_path = os.path.join(script_dir, "tests/actualDiff.txt")
    actual_file_path = os.path.join(script_dir, "tests/testDiff.txt")

    diffFile = open(diff_file_path,"r+")
    ls = diffFile.read().splitlines()
    actual = parse_diff(actual_file_path)
    i = 0
    for a in actual:
        if not a == ls[i]:
            return False
        #print a
        i = i + 1
        #print "size of actual" , len(actual[a])
        for z in actual[a]:
            if not z == ls[i]:
                return False
            i = i + 1
            #print z
    #print actual
    #print "got here"
    return True


if __name__ == '__main__':
    main()
