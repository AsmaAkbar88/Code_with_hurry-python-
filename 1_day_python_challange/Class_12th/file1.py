import random

computer_guess = random.randint(1, 10)
guess_number = 1
user_number = -1

while(user_number != computer_guess):
    user_number = int(input("Enter a guess Number:     "))
    if computer_guess > user_number:
        print("Choose high number:     ")
        guess_number += 1

    elif computer_guess < user_number:
        print("Choose Low number      ")
        guess_number += 1

print(f"You have gussed the number {user_number} correctly in {guess_number} attemps")