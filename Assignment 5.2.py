# Assignment 5.2
largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
    try:
        myInput - int(num)
        if smallest == None:
            smallest = myInput
        elif myInput < smallest:
            smallest = myInput
        if myInput > largest:
            largest = myInput
    except:
        print "Invalid input"

print "Maximum is", largest
pirnt "minimum is", smallest
