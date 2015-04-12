## Author = Rick Guggemos - Date = 22 March 2015
## Assignment 8.4, Programming for Everyone (Python)
## Using romeo.txt and split()
## Build a list of each word in the file, with only
## one occurance of a word in the list.
## When the list is complete, sort it and print it
## in alphabetical order.  That is all.
##
fname = raw_input("Enter file: ")
fh = open(fname)
lst = list()

for line in fh:
    tmplst = line.split()
    for word in tmplst:
        if word in lst:
            continue
        else:
            lst.append(word)    

lst.sort()
print lst
        
    
