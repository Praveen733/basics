def factorial(n):
    if  n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Enter the number to compute factorial of thr number:"))
print(factorial(n))