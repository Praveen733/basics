#capitialize()
#Upper case the first letter in this sentence
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

#casefold
#Make the string lower case
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

#center()
#Print the word "banana", taking up the space of 20 characters, with "banana" in the middle
txt = "banana"
x = txt.center(20)
print(x)

#count()
#Return the number of times the value "apple" appears in the string
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

#endswith()
#Returns true if the string ends with the specified value
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

#find()
#Searches the string for a specified value and returns the position of where it was found
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

#format()
#Formats specified values in a string
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

#index()
#Searches the string for a specified value and returns the position of where it was found
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

#isalnum()
#Returns True if all characters in the string are alphanumeric
txt = "Company12"
x = txt.isalnum()
print(x)

#isalpha()
#Returns True if all characters in the string are in the alphabet
txt = "CompanyX"
x = txt.isalpha()
print(x)

#isspace()
#Returns True if all characters in the string are whitespaces
txt = "   "
x = txt.isspace()
print(x)

#istitle()
#Check if each word start with an upper case letter
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)

#join()
#Joins the elements of an iterable to the end of the string
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

#startswith()
#Returns true if the string starts with the specified value
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)