list=[]
element=int(input("Enter how many elements you are going to add in  the list:"))
for i in range(0,element):
    ele=[int(input(":"))]
    list.append(ele)
    list.sort()
print("The smallest element in the list is",list[:1])