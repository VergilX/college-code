str1=input("input string: ")
str2=input("input string: ")
print(str1+str2)
if str1==str2:
    print("same")
else:
    print("Not same")
n=0
for i in str1:
    n+=1
print("length=",n)
str3=str1
print("Copied string: ", str3)
