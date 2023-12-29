def factorial(n):
    if (n == 0):
        return 1

    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans

def combination(n, r):
    return int(factorial(n) / (factorial(n-r)*factorial(r)))

n = int(input("Enter n: "))
for i in range(n+1):
    print(" " * (n-i), end="")
    
    for r in range(i+1):
        print(combination(i, r), end=" ")

    print()
