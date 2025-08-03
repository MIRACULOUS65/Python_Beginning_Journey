template="{},you r awesome u deserve this {}"

a="ram"
a1="car"
b="sam"
b1="bike"
c="jadu"
c1="scooty"

s1=template.format(a, a1)
s2=template.format(b, b1)
s3=template.format(c, c1)
print(s1)
print(s2)
print(s3)
print(f"{a}, you are awesome, you deserve this {a1}") #this is f-string formatting we can use variables directly by just using f"