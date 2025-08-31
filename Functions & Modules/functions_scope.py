def sum(a,b):
    # print(z)  # This will raise an error if z is not defined in the global scope but z is defined globally
    z=1 # This will raise an UnboundLocalError because z is assigned in the local scope which will destroy itself after the function call
    return a + b

z=8 #z is a global variable
print(sum(3, 4))  # This will print 7
print(z)  # This will print 8, the global variable z