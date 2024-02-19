from replit import clear

from art import logo

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a/b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def  calculator():
    print(logo)
    num1 = int(input("What's first number: "))
    for key in operations:
        print(key)

    end_of_program = False

    while not end_of_program:

        operation = input("Pick an operation from above ? ")

        num2 = int(input("What's next number: "))
        calculation_function = operations[operation]

        answer = calculation_function(num1, num2)

        print(f"{num1} {operation} {num2} = {answer}")
        not_end = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ")

        if not_end == 'y':
            num1 = answer
        else:
            end_of_program = True
            clear()
            calculator()

calculator()


