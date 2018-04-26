#!/usr/bin/python
from subprocess import call
import sys
import signal

def parse_diff():
  path_to_diffs = {}  # map from path to list of diff lines
  diffs = []
  path = None
  has_changes = False

  diff_file = open("/tmp/fullDiff.txt")
  lines = diff_file.read().splitlines()
  root_repo = lines.pop(0)  # path to the root of the repo

  # loop over lines, adding diffs to map
  for line in lines:
    if(line.startswith("+++")):
      has_changes = True
      path = root_repo + line[5:]

    # + and - and the beginning of a line signifies a change
    elif((line.startswith("+") or line.startswith("-")) and has_changes):
      diffs.append(line)
	
    # check if this is a new file
    if(line.startswith("diff") and has_changes):
      path_to_diffs[path] = diffs
      diffs = []
      path = None
      has_changes = False

  path_to_diffs[path] = diffs
  diff_file.close()

  return path_to_diffs

def run_multidelta(path_to_diffs):
  # takes a set, and concats into space seperated string
  files = ' '.join(str(path) for path in path_to_diffs.keys())
  multi = '~/multidelta'
  test_script = '~/commit-min/delta/mvn.test'
  unit_test = '-unit_test=' + str(sys.argv[1])

  run_delta = ' '.join([multi, unit_test, test_script, files])
  print run_delta
  #call(run_delta)

def interrupt_handler():
  # do something to kill multidelta and clean up files
  sys.exit(0)

def main():
  path_to_diffs = parse_diff() 
  run_multidelta(path_to_diffs)

if __name__ == '__main__':
  signal.signal(signal.SIGINT, interrupt_handler)
  main()

