from art import*
from replit import clear

def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

operations = {
"+":add,
"-":sub,
"*":mul,
"/":div,
}

def calculator():
    print(logo)
    n1 = float(input("What's the first number: "))
    for i in operations:
        print(i)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        n2 = float(input("What's the next number: "))
        calculation_function = operations[operation_symbol]  
        answer = calculation_function(n1, n2)
        print(f"{n1} {operation_symbol} {n2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            n1 = answer
        elif input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'n':
            should_continue = False
            calculator()

calculator()