import random

num = random.randint(1, 9)
print("guess a number between 1 and 9:")
guess = int(input("enter the number:"))

while True:

    if guess == num:
        print("(:!!You Won!!:)")
        break

    elif guess < num:
        print("the number you have chosen is to low!!")
        guess = int(input("enter the number:"))
        
    elif guess > num:
        print("the number you have chosen is to high!!")
        guess = int(input("enter the number:"))