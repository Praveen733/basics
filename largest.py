def max_num(num1,num2,num3):
    num1=int(input("Enter the number 1:"))
    num2=int(input("Enter the number 2:"))
    num3=int(input("Enter the number 3:"))
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
print("The largest number is", max_num('num1','num2','num3'))