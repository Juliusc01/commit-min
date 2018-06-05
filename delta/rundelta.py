#!/usr/bin/python
from subprocess import call
from collections import deque
import sys
import signal
import os

'''
takes the given path to a diff and creates a map from the files specified in the
diff to its corresponding changed lines and returns that mapping
'''
def parse_diff(full_path):
  path_to_diffs = {}  # map from path to list of diff lines
  diffs = []
  path = None
  has_changes = False

  diff_file = open(full_path)
  lines = diff_file.read().splitlines()

  # get a list of full paths for files that are not just refactors (we want to minimize)
  refactor = open("/tmp/refactorfiles.txt")
  refactor_files = refactor.read().splitlines()

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
      # don't include any paths that aren't in refactor files
      if path in refactor_files:
        path_to_diffs[path] = diffs
      diffs = []
      path = None
      has_changes = False

  # don't include any paths that aren't in refactor files
  if path in refactor_files:
    path_to_diffs[path] = diffs
  diff_file.close()
  refactor.close()

  return path_to_diffs

'''
takes a mapping between files and the changed lines and
sets it up to pass into calls run_delta from delta
'''
def run_multidelta(path_to_diffs):
  paths = path_to_diffs.keys()
  if not paths:
    return

  # takes a set, and concats into space seperated string
  files = ' '.join(str(path) for path in paths)

  # gets the directory this script is in, should be commit-min
  script_dir = os.path.dirname(os.path.realpath(__file__)) + '/'

  multi = script_dir + 'multidelta'
  test_script = script_dir + str(sys.argv[2])
  unit_test = '-unit_test=' + str(sys.argv[1])
  buggy_commit = '-bugid=' + str(sys.argv[3])

  run_delta = ' '.join([multi, unit_test, buggy_commit, test_script, files])
  call(run_delta, shell=True)



'''
Formats the changes given a path to the file
'''

def format_changes(full_path):
  path_to_diffs = {}  # map from path to list of diff lines
  diffs = []
  path = None
  has_changes = False
  other_lines = [] # for graph comparison
  diff_file = open(full_path)
  lines = diff_file.read().splitlines()
  root_repo = lines.pop(0)  # path to the root of the repo
  # loop over lines, adding diffs to map
  for line in lines:
    other_lines.append(line)
    if(line.startswith("+++")):
      has_changes = True
      path = root_repo + line[5:]

    # check if this is a new file
    if(line.startswith("diff") and has_changes):
      path_to_diffs[path] = diffs
      diffs = []
      path = None
      has_changes = False

  path_to_diffs[path] = diffs
  new_file = open("/tmp/diffOurs.txt", "w")
  new_file.write('\n'.join(other_lines))
  new_file.close()
  diff_file.close()

def interrupt_handler():
  # do something to kill multidelta and clean up files
  sys.exit(0)

def main():
  path_to_diffs = parse_diff("/tmp/fullDiff.txt") 
  run_multidelta(path_to_diffs)
  format_changes("/tmp/diffWithContext.txt")


if __name__ == '__main__':
  signal.signal(signal.SIGINT, interrupt_handler)
  main()

