#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys


# returns mimic dict that maps each word that appears in the file
# to a list of all the words that immediately follow that word in the file.
def mimic_dict(text):
    words_lst = text.split()  # splitting input text by spaces
    
    words_dict = {}
    for i in range(len(words_lst)-1):  # looping through words list
        if words_dict.get(words_lst[i]) == None:  # if the word is not a key
            words_dict[words_lst[i]] = words_lst[i+1]  # adding it as a key and consequent word as a value
        elif words_lst[i] in words_dict:  # if the word already is a key
            words_dict[words_lst[i]] += ',' + words_lst[i+1]  # adding it to the value separated my comma
    
    # splitting comma separated 'multi'-values into lists of words
    for key in words_dict:
        words_dict[key] = words_dict[key].split(',')
    
    # add to the dictionary an empty word key with value equal to the whole list of words from the text
    words_dict[''] = words_lst
    
    return words_dict


# takes mimic dict and a start word to print a 100 random words text
def print_mimic(d, w):
    lst = []
    for _ in range(100):  # range defines number of words in the final text
        lst.append(w)  # starting the list with the first word
        w = random.choice(d.get(w))  # randomly choosing the consecutive word from a list in values
        if w not in d:  # if randomly chosen word is not a key in the dictionary we return to ''
            w = ''
            
    # removing all '' from the text
    while '' in lst:
        lst.remove('')
    
    lst[0] = lst[0].title()  # making the first word of the text start with an upper case
    
    result = ' '.join(lst)  # creating the string with the text
    print(result)


# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print('usage: ./mimic.py file-to-read')
    sys.exit(1)

  filename = sys.argv[1]

  with open(filename) as file:
    content = file.read()

  dictionary = mimic_dict(content)
  print_mimic(dictionary, '')


if __name__ == '__main__':
  main()