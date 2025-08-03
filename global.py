def sum(a,b):
    print("hey I am summing")
    c=a+b
    global z  # Declare z as global to modify the global variable
    z=0 # Reset z to 0 in the global scope
    return c

z=15
print(sum(3, 4))  # This will print 7
print(z)  # This will print 15, the global variable z