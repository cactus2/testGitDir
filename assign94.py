##  Programming for Everyone (Python) - Assignment 9.4
##  Author Rick Guggemos - 4 April 2015
##  
##  Type "copyright", "credits" or "license()" for more information.
##  Write a program to read through the mbox-short.txt and figure out
##  who has the sent the greatest number of mail messages.  The
##  program looks for 'From ' lines and takes the second word of
##  those lines as the person who sent the mail.  The program creates
##  a Python dictionary that maps the sender's mail address to a
##  count of the number of times they appear in the file. After the
##  dictionary is produced, the program reads through the dictionary
##  using a maximum function.

counts = dict()
names = list()
fname = -1
bigname = None
bigcount = None
fhand = ()
tline = list()

fname = raw_input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
fhand = open(fname)

for line in fhand :
    if line.startswith('From: ') :
        tline = line.split()
        recipient = tline[1]
        names.append(recipient)

for recipient in names :
    counts[recipient] = counts.get(recipient, 0) + 1

for recipient,count in counts.items() :
    if bigcount is None or count > bigcount :
        bigname = recipient
        bigcount = count
print bigname, bigcount






    


