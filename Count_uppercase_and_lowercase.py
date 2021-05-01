def test_string(s):
    d={"Uppercase":0,"Lowercase":0}
    for i in s:
        if i.isupper():
            d["Uppercase"]+=1
        elif i.islower():
            d["Lowercase"]+=1
    print("Orginal string is:",s)
    print("Number of Uppercase letters are:",d["Uppercase"])
    print("Number of Uppercase letters are:",d["Lowercase"])
s=input("Enter the string:")
test_string(s)

        