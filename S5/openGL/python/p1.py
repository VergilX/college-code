from math import sqrt

a = int(input("Enter coeff of x^2: "))
b = int(input("Enter coeff of x: "))
c = int(input("Enter constant: "))

D = sqrt((b**2) - (4*a*c))
root1 = (-b + D) / (2*a)
root2 = (-b - D) / (2*a)

print("Roots: ", root1, root2)
