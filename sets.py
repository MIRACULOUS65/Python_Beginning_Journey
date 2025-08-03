s={3,5,8,10,12,15,18,20,25,30,35,40,45,50}

print(s,type(s))
s.add(55) # add a new element to the set 
print(s,type(s))
s.remove(10)
print(s,type(s))
print(s[3])  # This will raise an error since sets do not support indexing