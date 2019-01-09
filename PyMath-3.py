# PyMath-3 practising...

import math

x = int(raw_input("Enter a number: "))
y = int(raw_input("Enter a second number: "))
print "You entered " + str(x) + " and " + str(y)
print ""
option = raw_input("Choose an option: a for sum; b for multiplication or c for division.")
if option == "a":
    def optionSum(x, y):
        resultSum = x + y
        return resultSum
    
    print optionSum(x, y)
elif option == "b":
    def optionProduct(x, y):
        resultProduct = x * y
        return resultProduct
    
    print optionProduct(x, y)
elif option == "c":
    def optionDivision(x, y):
        resultDivision = x / y
        return resultDivision
    
    print optionDivision(x, y)
elif option == "exit":
    print "Goodbye!"
else:
    print "To exit type in exit."
    
while option == "a" or "b" or "c":
    x = int(raw_input("Enter a number: "))
    y = int(raw_input("Enter a second number: "))
    print "You entered " + str(x) + " and " + str(y)
    print ""
    option = raw_input("Choose an option: a for sum; b for multiplication or c for division.")
    if option == "a":
        def optionSum(x, y):
            resultSum = x + y
            return resultSum
        
        print optionSum(x, y)
    elif option == "b":
        def optionProduct(x, y):
            resultProduct = x * y
            return resultProduct
        
        print optionProduct(x, y)
    elif option == "c":
        def optionDivision(x, y):
            resultDivision = x / y
            return resultDivision
        
        print optionDivision(x, y)
    elif option == "exit":
        print "Goodbye!"
    else:
        print "To exit type in exit."    