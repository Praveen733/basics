import random
while True:
   name=input("Enter your name:")
   name2=input("Enter your crush name:")
   print(":)___LOVE CALCULATOR___:)")
   love=random.randint(97,100)
   print("Your love  is", love, "%")
   if love >=90:
       print("Your love is divine")
   elif love>=80:
       print("Your love is good")
   elif love>=70:
       print("Your love is worst,find a beter girl:")
   a=input("do you want to continue:")
   if a=="yes":
       continue
   else:
       break