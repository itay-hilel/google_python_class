#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.


# helper to sort a tuple by its last item    
def last(item):
    return item[-1]   


# function to count words and print them out alphabetical order
def print_words(content):
    oneline = content.replace('\n', ' ').lower()  # removing new line symbols
    words_list = oneline.split()  # spliting string into a list of words
    words_list.sort()  # sorting alphabeticaly our list of words
    words_dict = {}  
    count = 1  # setting count to one (if a word in a text it'll occure at least once)
    for i in range(len(words_list)-1):
        # the list is sorted, so if the prev word not the same as the next one it means it occures in the text only one time
        if words_list[i] != words_list[i+1]:  
            words_dict[words_list[i]] = count
            count = 1
        # if the prev word is equal to the next one we +1 to the occurance count
        else:
            count += 1
            words_dict[words_list[i]] = count
    # printing key-value pairs
    for key in words_dict:
        print(key, words_dict[key])


# function to count words and print out top 10 (ten appeared most frequent in the text)
def print_top(content):
    oneline = content.replace('\n', ' ').lower()  # removing new line symbols
    words_list = oneline.split()  # spliting string into a list of words
    words_list.sort()  # sorting alphabeticaly our list of words
    words_dict = {}  
    count = 1  # setting count to one (if a word in a text it'll occure at least once)
    for i in range(len(words_list)-1):
        # the list is sorted, so if the prev word not the same as the next one it means it occures in the text only one time
        if words_list[i] != words_list[i+1]:  
            words_dict[words_list[i]] = count
            count = 1
        # if the prev word is equal to the next one we +1 to the occurance count
        else:
            count += 1
            words_dict[words_list[i]] = count
    
    # printing top 10 most frequent key-value pairs
    empty = []  # creating empty list to put dict key-value pairs into list of tuples
    for key, value in words_dict.items():
        a = (key, value)
        empty.append(a)
    # sorting list of tuples by the last item in a tuple, i.e. word frequency
    empty_sorted = sorted(empty, key=last, reverse=True)[0:10]  # leaving only top 10
    # unfolding tuple while printing
    for t in empty_sorted:
        for i in range(len(t)-1):
            print(t[i], t[i+1]) 


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    with open(filename) as file:
      text = file.read()
    print_words(text)
  elif option == '--topcount':
    with open(filename) as file:
      text = file.read()
    print_top(text)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
