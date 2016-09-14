from capitals import capitals_dict
import random

correct_guess = False

while True:
    state = random.choice( list( capitals_dict.keys() ) )
    capital = capitals_dict[state]
 
    print("What is the capital of",state)
    guess = input("Guess: ")

    if guess.lower() == capital.lower():
        correct_guess = True
        break
    if guess.lower() == "exit":
        print("The answer is",capital)
        break

if correct_guess == True:
    print("Correct")
else:
    print("Goodbye.")
