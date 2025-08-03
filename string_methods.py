name=" sushovan "  # This is a single-line string
#name[0]="r" #strings are immutable, so this will raise an error we can change the value of a variable but not the string itself
a= len(name)  # This will give the length of the string, which is 8
print(a)  # This will print 8
print(name.upper())  # This will print the string in uppercase
print(name.lower())  # This will print the string in lowercase
print(name.title())  # This will print the string in title case
print(name.capitalize())  # This will capitalize the first letter of the string
print(name.isalnum())  # This will check if the string is alphanumeric (contains only letters and numbers)
print(name.isalpha())  # This will check if the string contains only letters
print(name.lstrip())  # This will remove leading whitespace from the string
print(name.rstrip())  # This will remove trailing whitespace from the string
print(name.strip())  # This will remove both leading and trailing whitespace from the string 

text="python is fun"
print(text.replace("fun", "awesome"))  # This will replace 'fun' with 'awesome' in the string
print(text.split())  # This will split the string into a list of words
print(text.find("is"))  # This will find the index of the substring 'is' in the string
print(text.index("is"))  # This will also find the index of the substring 'is' in the string
print(text.count("is"))  # This will count the number of occurrences of 'is'
print(",".join(["Python", "is", "awesome"]))  # This will join the list into a string with commas