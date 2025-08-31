# a=4
# b=2
# c=1


# average = (a + b + c) / 3
# print(average)

# a1=6
# b1=7
# c1=12


# average1 = (a1 + b1 + c1) / 3
# print(average1)

def average(a,b,c):
    d=(a + b + c) / 3
    return d

print(average(10, 20, 91))
# average(10, 20, 91) in this inside the function there should be a return function that returns the average value .  print(average(10, 20, 91)) is used to print the average value outside the function.

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
# this is f-string formatting we can use variables directly by just using f-strings, which is more readable and concise.