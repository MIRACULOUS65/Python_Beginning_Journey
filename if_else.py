# age =12
# if age < 18:
#     print("You are a minor.")
#     print("You are not an adult.")
# else:
#     print("You are an adult.")
#     print("You are not a minor.")

# print("This is the end of the program.")
# print("Thank you for using the program.")

age = int(input("Please enter your age: ")) #TypeError: '>' not supported between instances of 'str' and 'int' remember to convert input to int
 
if (age > 18):
   print("u can drive")
elif (age == 18):
    print("u can drive but u need to get a license")
else:
    print("u can't drive")
