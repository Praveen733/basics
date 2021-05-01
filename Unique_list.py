def unique_list(l):
    x=[]
    for i in l:
        if i not in x:
            x.append(i)
    return x
l=[1,2,1,2,3,3,4,5,6,7,8,7,9,10,9]
print(unique_list(l))