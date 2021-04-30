def test_range(n):
    if n in range(0,10):
        print("%s is in the range"%str(n))
    else:
        print("%s is outside in the given range"%str(n))
n=int(input("Enter the number:"))
test_range(n)