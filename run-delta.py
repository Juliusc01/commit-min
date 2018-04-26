#!/usr/bin/python
from subprocess import call

def main():
  dict1 = {}
  myFile = open("files.txt")
  lines = myFile.readlines()
  myList = []
  singleFile = None
  inChanges = False
  for line in lines:
    line = line[:-1]
    if(line.startswith("+++")):
      inChanges = True
      singleFile = line[6:]
    elif((line.startswith("+") or line.startswith("-")) and inChanges):
      myList.append(line)
	
    if(line.startswith("diff") and inChanges):
      dict1[singleFile] = myList
      myList = []
      singleFile = None
      inChanges = False

    dict1[singleFile] = myList
    myFile.close()
   

  # takes a set, and concats into space seperated string
  print dict1
  files = ' '.join(str(path) for path in dict1.keys())
  multi = '~/multidelta'
  test_script = '~/commit-min/delta/mvn.test'
  run_delta = multi + ' ' + test_script + ' ' + files
  #call(run_delta, shell=True)
  print files

if __name__ == '__main__':
  main()

