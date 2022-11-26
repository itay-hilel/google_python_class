#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
# LAB(begin solution)


# given a folder name returns a list of its special files (absolute path form)
def get_special_paths(folder):
  result = []
  paths = os.listdir(folder)  # lists files in the given folder
  for filename in paths:
    match = re.search(r'__(\w+)__', filename) # searches for the 'special' mask
    if match:  # if mask is True appends filename to a list containing special files names
      result.append(os.path.abspath(os.path.join(folder, filename))) 
  return result


# copies all of the given files to a given directory      
def copy_to(paths, to_dir):
  # creates a folder if it doesn't exist
  if os.path.exists(to_dir) == False:
    os.mkdir(to_dir)
  for path in paths:
    filename = os.path.basename(path)  # takes filename only (removes file to copy path)
    shutil.copy(path, os.path.join(to_dir, filename))  # joins filename and folder path where to copy
    # could error out if already exists os.path.exists():


# zips all of the given files to a new zip-file with a given name
def zip_to(paths, zipfile):
  cmd = 'zip -j ' + zipfile + ' ' + ' '.join(paths)
  print "Command I'm going to do:" + cmd
  (status, output) = commands.getstatusoutput(cmd)
  # If command had a problem (status is non-zero),
  # print its output to stderr and exit.
  if status:
    sys.stderr.write(output)
    sys.exit(1)

# LAB(end solution)


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  # LAB(begin solution)

  # Gather all the special files
  paths = []
  for dirname in args:
    paths.extend(get_special_paths(dirname))

  if todir:
    copy_to(paths, todir)
  elif tozip:
    zip_to(paths, tozip)
  else:
    print '\n'.join(paths)
  # LAB(end solution)

if __name__ == "__main__":
  main()
