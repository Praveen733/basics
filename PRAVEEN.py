#my_num=-70
#print(abs(my_num))
#print(round(7.3))
"""
name=input("Enter your name:")
age=int(input("Enter your year of birth:"))
age1=(2021-age)
print("Hello ",name," you are" ,age1)

def say_hi(name,age):
    print("hello ",name," you are ",age)
say_hi("Praveen", 20)

def cube(num):
    return num*num*num
num=int(input(''))
print(cube(num))

secret_word="praveen"
guess=""
guess_count=0
guess_limit=3
out_of_guesses=False
while guess != secret_word and not out_of_guesses:
    if guess_count <= guess_limit:
        guess=input("Enter your guess:")
        guess_count+=1
    else:
        out_of_guesses=True
if out_of_guesses:
    print("You lose")
else:
    print("you win")


friends=["PRAVEEN","MANSU","SATHISH","ASHIK"]
for friends in friends:
    print(friends)

number_grid=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
for col in number_grid:
    print(col)
print(number_grid[2][2])

"""
def translate(phrase):
    translation=""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation=translation+"B"
            else:
                translation=translation+"b"
        else:
            translation=translation+letter
    return translation
print(translate(input("Enter the phrase:")))