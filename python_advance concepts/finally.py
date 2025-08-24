def divide(a,b):
    try:
        c=a/b
        return c
    except Exception as e:
        print(e)

#this is always executed whether there is an exception or not
# finally block is used to execute the code that must be executed no matter what
#the reason to use finally block is to close the resources that are opened in the try block like file, database connection etc

    finally:
        print("I am always executed")


a=int(input("enter number 1: "))
b=int(input("enter number 2: "))

print(divide(a,b))