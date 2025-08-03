def add(a,b): #a,b arguments
    return a + b

c=add(10, 20) #10, 20 are passed as arguments to the function add
# add(10, 20) calls the function add with 10 and 20 as arguments
# c will hold the result of the addition
print(c)

def student(name, age): #name, age are parameters
    print (f"Name: {name}, Age: {age}")

student(age=20, name="Alice") #age=20, name="Alice" are keyword arguments
# student(age=20, name="Alice") calls the function student with age and name as keyword arguments
# this allows us to specify the arguments in any order

