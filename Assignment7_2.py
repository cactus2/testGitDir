#  Programming for Everyone (Python)
#  Assignment 7.2 - due 3/24/15
#  Rick Guggemos, author
#  Reading a file with Python
#  Selecting data strings, and
#  manipulating that data
#
#  Initialize accumulators
tcnfdlvl = 0
samplesz = 0
#
fname = raw_input('Enter file name: ')
try:                            
    bigfile = open(fname, 'r')  
    for line in bigfile:        
        if not line.startswith("X-DSPAM-Confidence:"): continue
        else:
            pos = line.find(':')
            spos = pos + 1
            xstr = line[spos:26]
            conlvl = xstr.lstrip()
            nmconlvl = float(conlvl)
            tcnfdlvl = tcnfdlvl + nmconlvl
            samplesz = samplesz + 1
    samplemean = tcnfdlvl / samplesz
    print 'Average spam confidence: ', samplemean
except:
    print 'File cannot be opened:', fname

    


