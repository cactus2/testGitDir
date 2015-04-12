##  Programming for Everyone (Python) - Assignment 10.2
##  Author Rick Guggemos - 5 April 2015
##  Tupling
##
##  Write a program to read through the mbox-short.txt and figure
##  out the distribution by hour of the day for each of the messages.
##  You can pull the hour out from the 'From ' line by finding the
##  time and then splitting the string a second time using a colon.
##
##  Once you have accumulated the counts for each hour, print out the
##  counts, sorted by hour as shown below.  Note that the autograder
##  does not have support for the sorted() function. 


counts = dict()
fname = ()
fhand = ()
fnlCut = list()
hours = list()
thour = list()
tline = list()
ttime = list()
pointr = 0

fname = raw_input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
fhand = open(fname)

for line in fhand :
    if line.startswith('From') :
        tline = line.split(' ')
        if len(tline) > 2 :
            ttime = tline[6]
            thour = ttime.split(':')
            hours.append(thour[0])
        
for ahour in hours :
    counts[ahour] = counts.get(ahour, 0) + 1

for key, val in counts.items() :
    fnlCut.append( (key, val) )
    
fnlCut.sort()

for key, val in fnlCut[:len(fnlCut)] :
    print key, val







    


