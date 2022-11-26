Hi there!


I'm intensively learning to code and interested in data science, aiming to be hired by the end of 2020.  
This repository is for completed projects and code snippets from [Google's Python Class](https://developers.google.com/edu/python)  

Official Description of the Class:
> "Welcome to Google's Python Class -- this is a free class for people with a little bit of
> programming experience who want to learn Python. The class includes written materials,
> lecture videos, and lots of code exercises to practice Python coding. These materials 
> are used within Google to introduce Python to people who have just a little programming 
> experience. The first exercises work on basic Python concepts like strings and lists, 
> building up to the later exercises which are full programs dealing with text files,
> processes, and http connections. The class is geared for people who have a little bit of
> programming experience in some language, enough to know what a "variable" or "if 
> statement" is. Beyond that, you do not need to be an expert programmer to use this
> material". 


### List of files and folders:
1. **my_hello.py** -- script to print 'Hello World!' or use a command line argument to greet a user with his name provided as a command line argument.
2. **my_string1.py** -- printing and slicing strings exercises.
3. **my_string2.py** -- slicing and using conditional statements strings exercises.
4. **my_list1.py** -- manipulatiing lists and sorting exercises.
5. **my_list2.py** -- custom sorting, manipulating lists and tuples exercises.  
6. **my_wordcount.py** -- counts how often each word appears in the text read from a file and prints words sorted in alphabetic oreder together with their occurance frequency counted ('--count' option) OR prints top ten most frequent words sorted by their occurance in the ascending order ('--topcount' option). Doesn't account for punctuation.  
Usage: python3 wordcount.py {--count | --topcount} filename.txt  
alice.txt -- *'Alice's Adventures in Wonderland'* full text to demonstrate my_wordcount.py script capabilities.
7. **my_mimic.py** -- builds a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file. Then takes mimic dict and prints a 100 random words text based on the mimic dict. Every time gives you a fun jibber-jabber output.  
e.g. based on *'Alice's Adventures in Wonderland' text*  
```
Attending to see what a won't you down the Gryphon; and every door
led into her hands and half down on in larger, I to get through
the be the Dodo replied rather the slowly back again with the
chimney close by taking the other guinea-pig immediately suppressed
I think (she was 'Up above a right distance--but then Alice dear!'
cried the air: it saw down from beginning to see you? And it'll
make out of them. The Rabbit noticed that this she could hear
oneself speak.
```  
8. **babynames** -- folder contains data with the most frequent 1000 babynames according to The Social Security administration US. The data is sorted by year and stored in html files (babynames_data.zip). **my_babynames.py** script reads data from html files, takes males and females babynames together with their ranks by use of Regular Expressions and prints out alphabetically sorted babynames data ([year, 'name rank', ... ]) or writes this data into a .txt file. After writing data into summary txt-files you can extract some cool insights about babynames trends, e.g. use *grep 'Trinity ' \*.txt* and you'll notice that after The Matrix movie was aired in 1999, name Trinity became literally 10 times more popular!  
9. **copyspecial** -- folder contains a script (**my_copyspecial.py**) and some data to run the script on. The script performs following tasks based on the provided command line arguments:  
- given a folder name returns a list of its special files (in an absolute path form)  
- copies all of the given files to a given directory  
- zips all of the given files to a new zip-file with a given name  
Usage: python2 my_copyspecial.py [--todir dir][--tozip zipfile] dir [dir ...]  
10. **logpuzzle** -- folder contains a script (**my_logpuzzle.py**) and data (**animal_code.google.zip** - first unzip the file to run the script on). The **result** folder contains results of running the script. The script performs following tasks:  
- reads the animal_code.google.com file and looks for links to download parts of an image
- removes duplicated links
- sorts the final list of links in an alphabetical order
- downloads parts of an image through links to a user specified folder
- renames the downloaded images and automatically creates an html file that you can open in a browser to see the whole image glued back together from the downloaded parts!  
Usage: python3 my_logpuzzle.py [--todir dir] file
  





  
Hope this repo will help you to assess my coding skills or will be just fun for you to play with.  



--------------------------------------------
Fill free to contact me via nktn.lx@gmal.com  
Follow me on twitter: @nktn_lx  
And here on github: github.com/nktnlx  