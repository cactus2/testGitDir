##  Python 2.7.9 (default, Dec 10 2014, 12:28:03) [MSC v.1500 64 bit (AMD64)] on win32
##  Type "copyright", "credits" or "license()" for more information.
##  Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail
##  messages.  The program looks for 'From ' lines and takes the second word of those lines as the person who sent
##  the mail.  The program creates a Python dictionary that maps the sender's mail address to a count of the number of times
##  they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum

counts = dict()
names = []
fname = -1
bigname = None
bigcount = None
fhand = ()
lst = ()
tline = list()
lastLine = 0

fname = raw_input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
fhand = open(fname)

for line in fhand :
    if len(line) < 1 :
        break
    if line[1:5] == '     ' :
        lastLine = lastLine + 1
        print lastLine
        continue
    else :
        tline = line.split()
        lastLine = lastLine +1
        print lastLine
        if tline[0] == 'From' :
            recipient = tline[1]
            print recipient
            names.append(recipient)
            print names
    
for recipient in names :
    counts[recipient] = counts.get(recipient, 0) + 1

for recipient,count in counts.items() :
    if bigcount is None or count > bigcount :
        bigname = recipient
        bigcount = count
print bigname, bigcount






    


