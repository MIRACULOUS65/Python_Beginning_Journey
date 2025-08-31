#write to a file called john doe.txt
# it should contain data about john doe

f= open("john doe.txt","wt") #by default it is in write mode and by adding t it is text mode and b is binary mode
f.write("John Doe is a fictional person often used to represent an anonymous or typical individual in legal proceedings, discussions, or examples. The name is commonly used in the United States and other English-speaking countries.\n")
f.close() #it is important to close the file after opening it
#in write mode if the file is not present it will create a new file with that name
# if the file is already present it will overwrite the existing content of the file
# to append data to the existing file we use append mode and not write mode w 
#so let's go try it in the next one
