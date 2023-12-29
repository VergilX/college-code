n=int(input("Enter the no ."))
a=n
sum=0
while(a>0):
    c=a%10
    sum+=c
    a=a//10
print("The sum of digits is",sum)

