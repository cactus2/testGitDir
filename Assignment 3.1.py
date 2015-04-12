#Pay in Py assignment 3.1

hrs = raw_input('Enter hours worked:\n')
try:
    Fhrs = float(hrs)
except:
    print 'Hours should be numeric'
    Fhrs = 0

rat = raw_input('Enter hourly rate:\n')
try:
    Frat = float(rat)
except:
    print 'Rate should be numeric'
    Frat = 0

if Fhrs > 0 and Frat > 0: # only compute with valid data
    if Fhrs <= 40:
        Pay = Frat * Fhrs
        print Pay
    elif Fhrs > 40
        BaseHrs = 40
        Basepay = BaseHrs * Frat
        Ohrs = Fhrs - BaseHrs
        Opay = Ohr * (Frat * 1.5)
        Pay = Basepay + Opay
        print Pay
