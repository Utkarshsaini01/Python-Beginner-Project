# for loops

# fruits = ["Apple", "Peach", "Pears"]

# for fruit in fruits:
#     print(fruit)

# # sum of even numbers

# target = int(input())

# total = 0;

# for i in range(2, target+1, 2):
#   total += i

# print(total)


#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))



# Easy level

# result = ""

# random.choice(list_name) choose random element from a list

# for i in range(0, nr_letters):
#     result += random.choice(letters)

# for i in range(0, nr_symbols):
#     # choose random element from a list
#     result += random.choice(symbols)

# for i in range(0, nr_numbers):
#     result += random.choice(numbers)

# print(result)






# Hard level

password_list = []

for i in range(0, nr_letters):
    password_list.append(random.choice(letters))

for i in range(0, nr_symbols):
    # choose random element from a list
    password_list.append(random.choice(symbols))

for i in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

# print(password_list)

random.shuffle(password_list)

# print(password_list)

password = ""

for char in password_list:
    password += char

print(password)





