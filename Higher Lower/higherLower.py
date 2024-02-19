# first get two random accounts for that
# import random
import random
from art import logo, vs
from replit import clear
# Step - 1: import the data and after
from game_data import data

def new_random_account():
  """Return a new random account"""
  return random.choice(data)


# Step - 2: format the data
def format_data(account):
  """Format the data accordingly for user experience"""
  
  name = account['name']
  description = account['description']
  country = account['country']

  return f"{name}, {description}, from {country}."

def check_answer(guess, a_follower, b_follower):
  """Check if the user guess correct or not. Returns a Boolean Value"""
  if(a_follower > b_follower):
      return guess == 'a'
  else:
      return guess == 'b'

def game():
  print(logo)
  account_a = new_random_account()
  account_b = new_random_account()
  
  game_over = False
  score = 0
  
  while not game_over:
    account_a = account_b
    account_b = new_random_account()
  
    while account_a == account_b:
      account_b = random.choice(data)
  
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
  
  
    guess = input("Who has more followers? Type 'A' or 'B':  ").lower()
  
    #Step 3: check if guess is correct
    follower_a = account_a['follower_count']
    follower_b = account_b['follower_count']
  
    clear()
    print(logo)
    if(check_answer(guess, follower_a, follower_b)):
      score += 1
      print(f"You are right. currect score: {score}")
    else:
      print(f"Sorry. That's Wrong. Final score: {score}")
      game_over = True


game()