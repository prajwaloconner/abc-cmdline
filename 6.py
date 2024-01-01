a=input("enter a sentence")
a=a.lower()
b=a.replace(" ","")
b=set(b)
b=list(b)
c=[]
for i in b:
    s=a.count(i)
    c.append(s)
d=c.index(max(c))
print(b[d],"appeared maximum number of times count=",c[d])
print(c)