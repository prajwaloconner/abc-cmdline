c=input("enter a string")
d=list(c)
f=""
g=0
e=['a','e','i','o','u','A','E','I','O','U']
for i in d:
    if i not in e:
        f+=i
    else:
        g+=1
print(f,"\ncount=",g)
print("consonants=",len(c.replace(" ",""))-g)
