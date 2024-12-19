#Calculator, where you can choose what operations you want to use
# this can be smarter way for selecting with operations to use. Check alt version where functions were put to dictionary

from calculator_ascii import logo
from os import system

def set_operation():
    which_operation = ""
    while which_operation not in operations:
        print("Select operation: ", *operations)
        which_operation = input()
    return which_operation

def operation_selection(first_number,second_number):
    if which_operation == "+":
        result = operation_add(first_number,second_number)
    if which_operation == "-":
        result = operation_minus(first_number,second_number)
    if which_operation == "*":
        result = operation_multiply(first_number,second_number)
    if which_operation == "/":
        result = operation_division(first_number,second_number)
    return result

def operation_add(number1,number2):
    return number1 + number2
def operation_minus(number1,number2):
    return number1 - number2
def operation_multiply(number1,number2):
    return number1 * number2
def operation_division(number1,number2):
    return number1 / number2


operations = ["+", "-","*","/"]
which_operation = "placeholder"
new_operation = True
result = 0
print(logo)


while True:
    if new_operation == True:
        first_number = round(float(input("Provide first number: ")),2)
        new_operation = False
    which_operation = set_operation()
    second_number = round(float(input("Provide another number: ")),2)
    result = round(float(operation_selection(first_number, second_number)),2)
    print(f"{first_number} {which_operation} {second_number} = {result}")
    
    another_one = input("Want to continue?\n[n] - new calculation, [c] - continue with previous result, anything else - exit: ")
    if another_one == "n":
        new_operation = True
        system("cls")
    elif another_one == "c":
        first_number = result
    else:
        break