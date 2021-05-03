def even_number(e):
    enumber=[]
    for i in e:
        if i % 2 == 0:
            enumber.append(i)
    return enumber
e=[1,2,3,4,5,6,7,8,9,10]
print(even_number(e))