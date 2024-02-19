from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.
print(art.logo)

print("Welcome to the secret auction program. ")

def highest_bidder(bids):
  highest_amount = 0
  winner = ""

  for bidder in bids:
    amount = bids[bidder]
    if(amount > highest_amount):
      highest_amount = amount
      winner = bidder

  print(f"The winner is {winner} with a highest bid of ${highest_amount}")



auction = {}

end_of_program = False

while not end_of_program:
  
  name = input("What is your name? ")
  bid = int(input("What's your bid? $"))

  auction[name] = bid

  end = input("Are there any other bidders? Type 'yes' or 'no' : ")



  if end == 'no':
    end_of_program = True
  
  clear()
  
  
# print(auction)
highest_bidder(auction)
