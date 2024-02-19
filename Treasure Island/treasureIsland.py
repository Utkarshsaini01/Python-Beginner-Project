print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
dir = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' \n")

if(dir == 'left'):
    isswim = input("You come to a lake. There is an island in the middle of the lake. Type 'swim' to swim across. Type 'wait' to wait for a boat.\n")
    
    if(isswim == 'wait'):
        color = input("You arrive at the island unharmed. There is a house with 3 doors. One red, on yellow and on blue. which color do you choose?\n")
        if(color == "yellow"):
            print("Congratulations !! You found the Treasure!!")
        elif(color == "red"):
            print("Burned by fire. Game Over!!")
        elif(color == "blue"):
            print("Eaten by beasts. Game Over!!")
        else:
            print("Game over!!")
    else:
        print("Attacked by trout. Game Over!!")
else:
    print("Fall into a hole. Game Over!!")
