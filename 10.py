def calsi(s,r,cost):
    if(cost>r):
        print("u have no funds remaining or insufficient funds")
        return 0,0,0
    else:
        s=s+cost
        r-=cost
        return s,r,cost
def main():
    ts=0
    a=int(input("enter total budget or available funds "))
    r=a
    b=0
    for i in range (1,8):
        print("day ",i)
        while(True):
            c=input("press y if you have spent money today or want to add data")
            if(c=="y" or c=="Y"):
                d=int(input("enter cost spent"))
                e,f,g=calsi(b,r,d)
                ts+=e
                break
            else:
                c=input("press y to go to next day or anything else to stay in the same day")
                if c=='y' or c=="Y":
                    break
                else:
                    print("staying in the same day")
        print ("day ",i,"spent:remaining=",ts,a-ts,sep=":")
main()