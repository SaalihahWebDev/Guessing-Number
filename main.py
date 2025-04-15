import random
number=random.randint(1,10)
guess=None
tries=0
print("Welcome to the guessing game🔍🔍🔍🔍")
print("I am thinking of a number from 1 to 10🤔🤔.Can you help me find it🔍🔍")
while guess!=number:
    try:
        guess=int(input("Enter your guess: "))
        tries+=1
        if guess<=number:
            print("Too low.Try Again")
        elif guess>=number:
            print("Too high.Tell something lower")
    except ValueError:
        print("Please Enter a value Number")
print(f"🎉🎉🎉🎉You got it,The number was {number} ")
print(f"It got you {tries} tries")