import random
#1 Generate random numbers for player and computer
player_number = random.randint(1, 100)
computer_number = random.randint(1, 100)
#2 Print numbers for testing
print(f"Player's number: {player_number}")
print(f"Computer's number: {computer_number}")
#3 Ask the user for their guess
user_guess = input(f"Your number is {player_number}. Do you think your number is higher or lower than the computer's? (type 'higher' or 'lower'): ").strip().lower()

#4 Display user's input
print(f"You guessed: {user_guess}")
#5 Compare numbers and determine correctness
if (user_guess == "higher" and player_number > computer_number) or (user_guess == "lower" and player_number < computer_number):
    print(f"You were right! The computer's number was {computer_number}.")
else:
    print(f"Aww, that's incorrect. The computer's number was {computer_number}.")
    NUM_ROUNDS = 5
score = 0

for round in range(1, NUM_ROUNDS + 1):
    print(f"\nRound {round}")
    
    #6 Generate new numbers for each round
    player_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)
    
    #7 Ask for user input
    user_guess = input(f"Your number is {player_number}. Do you think your number is higher or lower than the computer's? (type 'higher' or 'lower'): ").strip().lower()
    
    #8 Game logic
    if (user_guess == "higher" and player_number > computer_number) or (user_guess == "lower" and player_number < computer_number):
        print(f"You were right! The computer's number was {computer_number}.")
        score += 1
    else:
        print(f"Aww, that's incorrect. The computer's number was {computer_number}.")

    #9 Display score
    print(f"Your score is now {score}.")

while user_guess not in ["higher", "lower"]:
    user_guess = input("Please enter 'higher' or 'lower': ").strip().lower()
# 10 Ending message based on performance
print("\nThanks for playing!")
if score == NUM_ROUNDS:
    print("Perfect score! You really know your numbers!")
elif score > NUM_ROUNDS / 2:
    print("Good job! You did well!")
else:
    print("Better luck next time!")
import random

NUM_ROUNDS = 5
score = 0

print("Welcome to the High-Low Game!")
print("--------------------------------")

for round in range(1, NUM_ROUNDS + 1):
    print(f"\nRound {round}")
    
    player_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)
    
    user_guess = input(f"Your number is {player_number}. Do you think your number is higher or lower than the computer's? (type 'higher' or 'lower'): ").strip().lower()

    while user_guess not in ["higher", "lower"]:
        user_guess = input("Please enter 'higher' or 'lower': ").strip().lower()
    
    if (user_guess == "higher" and player_number > computer_number) or (user_guess == "lower" and player_number < computer_number):
        print(f"You were right! The computer's number was {computer_number}.")
        score += 1
    else:
        print(f"Aww, that's incorrect. The computer's number was {computer_number}.")

    print(f"Your score is now {score}.")

#11 Ending message based on performance
print("\nThanks for playing!")
if score == NUM_ROUNDS:
    print("Perfect score! You really know your numbers!")
elif score > NUM_ROUNDS / 2:
    print("Good job! You did well!")
else:
    print("Better luck next time!")




