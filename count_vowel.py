def vowel(s):
    count=0
    index=0
    res=[]
    for vowel in s:
        index+=1
        if vowel.lower() in "aeiou":
            count=count+1
    print("number of vowels in",s,"are:",count)
s=input("Enter the string:")
vowel(s)
