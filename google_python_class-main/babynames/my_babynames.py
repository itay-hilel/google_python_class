#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  with open(filename) as file:
    text = file.read()
  # extracting year to a list    
  year = re.findall(r'Popularity in (\d\d\d\d)', text)
  # extracting rank and names to a list
  names_list = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)
    
  # creating name:rank dictionary
  names_dict = {}
  for tup in names_list:
    names_dict[tup[1]] = tup[0]
    names_dict[tup[2]] = tup[0]
    
  # building the [year, 'name rank', ...] list    
  result = []
  result.append(year[0])
  for key in sorted(names_dict):
    result.append(key + ' ' + names_dict[key])
    
  return result


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for filename in args:
    names = extract_names(filename)
    output = '\n'.join(names)

    if summary:
      new_file = open(filename[:-5] + '_summary.txt', 'w')
      new_file.write(output + '\n')
      new_file.close()
    else:
      print(output)
  
if __name__ == '__main__':
  main()