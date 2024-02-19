import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def compare(num, guess):
    """ Compare the numbers and return the result """
    if(num == guess):
        return f"You got it! The answer was {num}."
    elif(num < guess):
        return "Too high.\nGuess Again"
    else:
        return "Too Low.\nGuess Again"

def set_difficulty():
    """ Get the difficulty level as input and return the number of attempts according to that """
    
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if(difficulty == 'easy'):
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    num = random.randint(1, 100)
    
    no_of_attempts = set_difficulty()
    
    
    while no_of_attempts > 0:
        print(f"You have {no_of_attempts} remaining to guess the number. ")
        guess = int(input("Make a guess: "))
        
        print(compare(num, guess))
        if(num == guess):
            return
            
        no_of_attempts -= 1
        
        if(no_of_attempts == 0):
            print("You've run out of guesses, you lose.")


game()