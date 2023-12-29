print("Menu 1. add 2.sub 3.mul 4.div 5.exit")
ch=int(input("enter ur choice"))
while ch!=5:
    a=int(input("enter no."))
    b=int(input("enter no."))
    if ch==1:
        print(a+b)
    elif ch==2:
        print(a-b)
    elif ch==3:
        print(a*b)
    elif ch==4:
        print(a/b)
    else:
        print("invalid choice")
    ch=int(input("enter ur choice"))

print("Terminating")

