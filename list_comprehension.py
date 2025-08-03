a=5

# table = []  # creating an empty list to store the multiplication table
# for i in range(1, 11):
#     table.append(a * i)

#the whole thing in shorter way
table = [a * i for i in range(1, 11)]  # list comprehension to create the multiplication table

print(table)  # printing the multiplication table of 5

#also see the short note