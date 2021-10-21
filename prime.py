start=int(input("Enter the start point:"))
end=int(input("Enter the end point:"))
for i in range(start,end):
    for j in range(2,i):
        if (i%j)==0:
            break
    else:
        print(i)