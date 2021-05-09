def pure_func(list):
    New_list=[]
    for i in list:
        New_list.append(i**2)
    return New_list
orginal_list=[1,3,5,7]
modified_list=pure_func(orginal_list)
print("Orginal list:",orginal_list)
print("Modified list:",modified_list)

