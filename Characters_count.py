def char_frequency(str1):
    dict={}
    for n in str1:
        keys=dict.keys()
        if n in keys:
            dict[n]+=1
        else:
            dict[n]=1
    return dict
def char_count(str1):
    count=0
    for n in str1:
        count+=1
    return count
str1="Good Morning"
print(char_frequency(str1))
print(char_count(str1))