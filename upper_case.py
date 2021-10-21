a=input("Enter the sentence:")
count=0
count1=0
for i in a:
    if i.isupper():
        count=count+1
    elif i.islower():
        count1=count1+1 
print("Number of upper case letters are:",count)
print("Number of lower case letters are:",count1)