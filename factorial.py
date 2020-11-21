def factorial(n):
    fact=1
    if n < 0 :
        return 0
    elif n ==0 or n ==1:
        return 1
    else:
        for i in range(1,n+1):
            fact=fact*i
        print("the factorial of",n,"is",fact)
n=int(input("Enter the number:"))
factorial(n)