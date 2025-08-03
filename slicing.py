name="sushovan"  # This is a single-line string
print(name[0:2]) # This will print the first two characters 'su'
print(name[2:-1])  # This will print characters from index 2 to the end, which is 'shovan' 
print(name[0:7:1]) # This will print the entire string 'sushovan'(1-1=0)

print(name[0:7:2]) # This will print every second character from the string,from index 0 to 6, which is 's-s-o-a'(2-1=1)
print(name[::2])  # This will print every second character from the entire string, which is 's-s-o-a'
print(name[::-1])  # This will print the string in reverse order, which is 'navohsus'