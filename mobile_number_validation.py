import re
def isValid(s):
    pattern=re.compile("(0/91)?[7-9][0-9]{9}")
    return pattern.match(s)
s=(input("Enter The Mobile Number With Country Code:"))
if (isValid(s)):
    if len(s) >= 12:
        print("Number is valid")
    else:
        print("Number is not valid")
else:
    print("Enter a valid number")
