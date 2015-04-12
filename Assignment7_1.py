#  Programming for Everyone (Python)
#  Assignment 7.1 - due 3/24/15
#  Rick Guggemos, author
#  Reading a file with Python
#
fname = raw_input('Enter file name: ')
#
try:                                # Present error if file
    cantaloupe = open(fname, 'r')   # can't be opened.
    for seeds in cantaloupe:        # Read line by line
        seeds = seeds.rstrip()      # to end of file.
        print seeds.upper()
except:
    print 'File cannot be opened:', fname
    


