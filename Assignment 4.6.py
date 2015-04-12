#!/usr/bin/python
def computepay(hrs,rat):
    if hrs <= 40:
        tpay = hrs * rat
        return(tpay)
    elif hrs > 40:
        basepay = 40 * rat
        ohrs = hrs - 40
        opay = ohrs * (rat * 1.5)
        tpay = basepay + opay
        return(tpay)
    else:
        print "Houston we have a problem"

rhrs = raw_input('Enter Hours Worked:\n')
rrat = raw_input('Enter Hourly Rate:\n')

try:
    Fhrs = float(rhrs)
    Frat = float(rrat)
    pay = computepay(Fhrs,Frat)
except:
    pay = 'Please enter a number'

print(pay)