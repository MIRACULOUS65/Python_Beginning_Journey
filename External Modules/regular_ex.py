import re 
text ="the quick brown fox jumps over the lazy dog"
match=re.search("fox",text)
print(match)  #span=(16,19) means it is present from index 16 to 19
if match:
    print("match found")
    print("start index:",match.start())
    print("end index:",match.end())

matches=re.findall("the",text,re.IGNORECASE)
print(matches)
new_text=re.sub("the","a",text)
print(new_text)