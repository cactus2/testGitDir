##  Exercise 6.5
##  Programming for Everybody (Python)
##  6 March 2015  -  Rick Guggemos

str = 'X-DSPAM-Confidence:  0.8475'

pos = str.find(":")

spos = pos + 1
 
x = str[spos:40]
 
basics = x.lstrip()
 
ans = float(basics)

print ans
