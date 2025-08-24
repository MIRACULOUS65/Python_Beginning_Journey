# while True:
#     try:
#         a=int(input("enter number 1: "))
#         b=int(input("enter number 2: "))
#         print(f"The division of {a} and {b} is {a/b}")

#     except ValueError as e:
#         print("Invalid input please enter numbers only",e)
    
#     except ZeroDivisionError as e:
#         print("Division by zero is not allowed",e)

#     except Exception as e:
#         print("Invalid input please try again",e)


a=int(input("enter number 1: "))
b=int(input("enter number 2: "))

if b==0:
    raise ZeroDivisionError("Division by zero is not allowed")

print(f"The division of {a} and {b} is {a/b}")