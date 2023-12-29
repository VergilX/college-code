N1=int(input("Enter the no. of columns of first matrix"))
M1=int(input("Enter the no. of rows of first matrix"))

N2=int(input("Enter the no. of columns of second matrix"))
M2=int(input("Enter the no. of rows of second matrix"))
l1=[]
l2=[]
def matrix_init(l,x,y):
    temp=[]
    for i in range(x):
        for j in range(y):
            a=int(input("enter the matrix",i,"row",j,"column"))
            temp+=[a]
        l+=[temp]
def matrix_display(l,x,y):
   for i in range(x):
        for j in range(y):
            print(l[i][j],end=" ")
        print()

if (N1==M2):
    print("First Matrix")
    matrix_init(l1,M1,N1)
    matrix_display(l1,M1,N1)
    print("Second Matrix")
    matrix_init(l2,M2,N2)
    matrix_display(l2,M2,N2)
    for i in range(




            
