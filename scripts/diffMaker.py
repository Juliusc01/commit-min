#!/usr/bin/python
from subprocess import call
from collections import deque
import sys
import signal
import os

def parse_diff(full_path, which_one):
  has_changes = False
  new_lines = []
  diff_file = open(full_path)
  lines = diff_file.read().splitlines()
  root_repo = lines.pop(0)  # path to the root of the repo
  # loop over lines, adding diffs to map
  for line in lines:
    if(line.startswith("+++")):
      has_changes = True
    # + and - and the beginning of a line signifies a change
    elif((line.startswith("+") or line.startswith("-")) and has_changes):
      new_lines.append(line)
    # check if this is a new file
    if(line.startswith("diff") and has_changes):
      has_changes = False

  new_file = open("/tmp/diff"+str(which_one)+".txt", "w")
  for item in new_lines:
    new_file.write("%s\n" % item)
  new_file.close()
  diff_file.close()

def interrupt_handler():
  sys.exit(0)
  
def main():
  path_to_diffs = parse_diff("/tmp/fullDiff.txt", "Other")
  path_to_diffs = parse_diff("/tmp/diffOurs.txt", "NewOurs")

if __name__ == '__main__':
  signal.signal(signal.SIGINT, interrupt_handler)
  main()
