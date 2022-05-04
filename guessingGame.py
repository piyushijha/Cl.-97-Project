import random

print("Number guessing game")

number = random.randint(1,9)
chances = 0
print("Guess a number between 1 to 9")


while chances < 5: 
    guess = int(input("Enter your guess: "))
    
    if  guess ==  number: 
        print("Congratulations YOU WON!!!")
        break 

    chances += 1


if not chances < 5: 
    print("YOU LOSE!!! The number is", number)