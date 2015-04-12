#Grade Range in Py - Assignment 3.3

score = raw_input('Please enter a score between 0.0 and 1.0:\n')
try:
    Fscore = float(score)
except:
    print 'Score should be numeric'
    quit()

if Fscore > 1.0:       #looking for valid data range
    print 'Maximum score = 1.0'
    quit
elif Fscore < 0.0
    print 'Minimum score = 0.0'
    quit()

if Fscore >= 0.9:    #Assigning Letter Grades
    Grade = 'A'
elif Fscore >= 0.8:
    Grade = 'B'
elif Fscore >= 0.7:
    Grade = 'C'
elif Fscore >= 0.7:
    Grade = 'D'
else:
    Grade = 'F'    #Someone is in trouble

print Grade