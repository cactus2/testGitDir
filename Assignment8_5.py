## Author = Rick Guggemos - Date = 22 March 2015
## Assignment 8.5, Programming for Everyone (Python)
## Using mbox-short.txt and split()
## Check for lines beginning with "From ", not "From:"
## For the selected lines, convert to list and print
## the second element which is the email address.
## Count the number of selected lines, and print out a
## message relating that count.
##
fname = raw_input("Enter file: ")
fh = open(fname)
counter = 0

for line in fh:
    line = line.rstrip()
    if line.startswith('From '):
        tmplst = line.split()
        print tmplst[1]
        counter = counter + 1

print "There were", counter, "lines in the file with From as the first word"    

        
    
