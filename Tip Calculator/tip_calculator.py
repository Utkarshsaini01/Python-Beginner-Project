print("Welcome to the tip calculator.")
bill = float(input("What was the total bill ? $ "))
percent = int(input("What percentage tip would you like to give? 10, 12, or 15 ? "))

total = bill + bill*percent/100

no_people = int(input("How many people to split the bill ? "))

each_share = total/no_people
# each_share = round(total/no_people, 2)

# another way to round off
each_share = "{:.2f}".format(each_share)

print(f"Each person should pay: ${each_share}\n")
