def ftoc(f):
    c=0.0
    c=(f-32)*(5/9)
    c=round(c,5)
    return c
def ctof(c):
    f=0.0
    f=round(((c*(9/5))+32),5)
    return f
def main():
    b=int(input("enter a number"))
    try:
       a=int(input("1.f to c \n 2 .c to f\n enter choice"))
       if(a==1):
            print(ftoc(b))
       else:
            print(ctof(b))
            
             
    except:
        print("error")
main()
    
    

    