import random
def main():
    print("a random number will be generated guess it in 5 attempts")
    c=5
    ch=games()
    while(c>0):
        a=int(input("enter number"))
        if(a==ch):
            break
        b=abs(a-ch)
        if (b<11):
            print("almost there")
        else:
            print("too far")
        c-=1
    print("Game score=",c*20)
def games():
    a=random.randint(1,100)
    return a
main()