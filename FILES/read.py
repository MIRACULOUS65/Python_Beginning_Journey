f= open("mrcls.txt","rt") #by default it is in read mode and by adding t it is text mode and b is binary mode

content=f.read() #it will read the whole file
print(content)

f.close() #it is important to close the file after opening it