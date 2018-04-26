#!/user/bin/python

def main():
    testParseDiff()

def testParseDiff():
    diffFile = open("../tmp/fullDiff.txt")
    readDiff = open("testDiff.txt")
    ls = readDiff.read().splitlines()
    for l in ls:
        diffFile.write(l)
    actual = parseDiff()
    print actual


if __name__ == '__main__':
    main()
