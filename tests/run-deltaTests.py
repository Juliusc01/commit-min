#!/user/bin/python
import sys
#sys.path.append('../')
from .. import rundelta

def main():
    testParseDiff()

def testParseDiff():
    diffFile = open("../tmp/fullDiff.txt","w+")
    readDiff = open("testDiff.txt","w+")
    ls = readDiff.read().splitlines()
    for l in ls:
        diffFile.write(l)
    actual = parse_diff()
    print actual


if __name__ == '__main__':
    main()
