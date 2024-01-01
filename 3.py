import time
def names(s):
    print("hello",s)
def ntime(s):
    a=time.localtime()
    c=time.strftime("%H,%M:%S",a)
    d=time.strftime("%H",a)
    print(a,d,sep="\n")
    if 6<int(d)<12:
        print("Morning",s)
    elif 12<int(d)<16:
        print("Evening",s)
    else:
        print("good night",s)
def main():
    a=input("enter name ")
    names(a)
    ntime(a)
main()
