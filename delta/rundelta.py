#!/usr/bin/python
from subprocess import call
from collections import deque
import sys
import signal
import os

def parse_diff(full_path):
  path_to_diffs = {}  # map from path to list of diff lines
  diffs = []
  path = None
  has_changes = False

  diff_file = open(full_path)
  lines = diff_file.read().splitlines()

  # get a list of full paths for files that are not just refactors (we want to minimize)
  #refactor = open("/tmp/refactorfiles.txt")
  #refactor_files = refactor.read().splitlines()

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
      #if path in refactor_files:
      path_to_diffs[path] = diffs
      diffs = []
      path = None
      has_changes = False

  # don't include any paths that aren't in refactor files
  #if path in refactor_files:
  path_to_diffs[path] = diffs
  diff_file.close()
  #refactor.close()

  return path_to_diffs

def run_multidelta(path_to_diffs):
  # takes a set, and concats into space seperated string
  files = ' '.join(str(path) for path in path_to_diffs.keys())

  # gets the directory this script is in, should be commit-min
  script_dir = os.path.dirname(os.path.realpath(__file__)) + '/'

  multi = script_dir + 'multidelta'
  test_script = script_dir + str(sys.argv[2])
  unit_test = '-unit_test=' + str(sys.argv[1])
  buggy_commit = '-bugid=' + str(sys.argv[3])

  run_delta = ' '.join([multi, unit_test, buggy_commit, test_script, files])
  call(run_delta, shell=True)

def find_reverts(path_to_diffs):
  path_to_reverts = {}
  reverts = deque([])  # keep reverts in a queue
  for path, diffs in path_to_diffs.iteritems():
    curr_file_str = open(path).read()

    # loop through diffs to see if they are still in file
    for diff in diffs:
      if diff.startswith("+"):
        diff = diff[1:]  # remove + from diff and search in file
        if diff not in curr_file_str:
          reverts.append(diff)

    path_to_reverts[path] = reverts

  return path_to_reverts

def revert_changes(path_to_reverts):
  for path, reverts in path_to_reverts.iteritems():
    curr_revert = None

    # no need to read the file if there is nothing to revert
    if reverts:
      curr_revert = reverts.popleft()
    else:
      continue

    # read from the backup file before delta ran
    backup_file = open(path + ".bak", "r")
    backup_file_lines = backup_file.readlines()
    new_lines = []

    # do not include any reverts in new_lines
    for line in backup_file_lines:
      if curr_revert in line:
        if reverts:
          curr_revert = reverts.popleft()
      else:
        new_lines.append(line)

    if reverts:
      sys.exit('There should not be anything left in reverts queue')

    # write the new lines to the original file
    orig_file = open(path, "w")
    orig_file.writelines(new_lines)
    orig_file.close()
    backup_file.close()

def print_new_changes(full_path, path_to_reverts):
  path_to_diffs = {}  # map from path to list of diff lines
  diffs = []
  path = None
  has_changes = False
  new_lines = []
  other_lines = [] # for graph comparison
  diff_file = open(full_path)
  lines = diff_file.read().splitlines()
  root_repo = lines.pop(0)  # path to the root of the repo
  # loop over lines, adding diffs to map
  for line in lines:
    other_lines.append(line)
    new_lines.append(line)
    if(line.startswith("+++")):
      has_changes = True
      path = root_repo + line[5:]
      #print(path)
      #print(path_to_reverts)
    # + and - and the beginning of a line signifies a change
    elif((line.startswith("+") or line.startswith("-")) and has_changes):
      if(path_to_reverts.get(path)):
        if(path_to_reverts.get(path).popleft() == line[1:]):
          new_lines.remove(line)
          new_lines.append("this line has been removed from the commit: " + line[1:])

    # check if this is a new file
    if(line.startswith("diff") and has_changes):
      path_to_diffs[path] = diffs
      diffs = []
      path = None
      has_changes = False

  path_to_diffs[path] = diffs
  for line in new_lines:
    print line
  new_file = open("/tmp/diffOurs.txt", "w")
  new_file.writelines(other_lines)
  new_file.close()
  diff_file.close()

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
  #path_to_reverts = find_reverts(path_to_diffs)
  #print_new_changes("/tmp/diffWithContext.txt", path_to_reverts)
  #revert_changes(path_to_reverts)

if __name__ == '__main__':
  signal.signal(signal.SIGINT, interrupt_handler)
  main()

