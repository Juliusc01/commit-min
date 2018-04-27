#!/user/bin/python
#import sys
#sys.path.append('../')
from rundelta import parse_diff

def main():
    return testParseDiff()

def testParseDiff():
    diffFile = open("tests/actualDiff.txt","r+")
    ls = diffFile.read().splitlines()
    #readDiff = open("tests/testDiff.txt","r+")
    #ls = readDiff.read().splitlines()
    #for l in ls:
    #    diffFile.write(l)
    #actual = parse_diff("tests/testDiff.txt")
    actual = parse_diff("tests/testDiff.txt")
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
