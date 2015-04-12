Python 2.7.9 (default, Dec 10 2014, 12:24:55) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Pay in Py assignment 3.1

hrs = raw_input('Enter Hours Worked:\n')
try:
    Fhrs = float(hrs)
except:
    print 'Hours should be numeric'
    Fhrs = 0
    
rat = raw_input('Enter Hourly Rate:\n')
try:
    Frat = float(rat)
except:
    print 'Rate should be numeric'
    Frat = 0

if Fhrs > 0 and Frat > 0:   
    if Fhrs <= 40:
        Pay = Frat * Fhrs
        print Pay

    elif Fhrs > 40:
        Basepay = 40 * Frat
        Ohrs = Fhrs % 40
        Opay = Ohrs * (Frat * 1.5)
        Pay = Basepay + Opay
        print Pay
