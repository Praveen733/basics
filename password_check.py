username=input("Enter the username:")
password=input("Enter the password:")
a=["Jithu","Santhu","Sushama"]
b=["Menden","Tarz","Udayipp"]
if username in a:
    if password in b:
        print("Welcome",username)
    else:
        print("Invalid username or password")