a=6
guess=""
while guess != a:
    guess=int(input("Enter Your Guess:"))
    if a < guess:
        print("Guess a low value")
    if a > guess:
        print("Guess a high value")
    elif a == guess:
        print("______You win ginga lalaa____")
