import random
Secret_no = random.randint(1,50)
print("Welcome to the number guessing game. we have number that needs to guessed.")
print("Secret no. is between 1 to 50")
choice = int(input("enter how many attempts you want: "))
print("\n")
print(f"you have {choice} attempts left")
attempt = 0
counter = choice
for i in range(counter):
    value = int(input("enter your guess: "))
    counter -=1
    attempt +=1
    if value > Secret_no:
        print("Your guess is wrong! Try Lower")
        print(f"you have {counter} attempt left")
    elif value < Secret_no:
        print("Your guess is wrong! Try Higher")
        print(f"you have {counter} attempt left")
    else:
        print("\n")
        print("congrats your guess is correct")
        print(f"The number was {Secret_no} and you take {attempt} attempt, Game Over!")
        break
if counter == 0 and value != Secret_no:
    print("You lost the game!")
    print(f"the number was {Secret_no}.")