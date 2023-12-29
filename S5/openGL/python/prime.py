n = int(input("Enter range: "))

def is_prime(n):
    for i in range(2, n//2+1):
        if (n%i == 0):
            return False

    return True

for i in range(1, n+1):
    if is_prime(i):
        print(i)
