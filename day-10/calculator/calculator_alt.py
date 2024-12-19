import calculator_ascii

def add(n1, n2):
    return n1+ n2

def substract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

def calculator():
    operations = {"+": add,
            "-": substract,
            "*": multiply,
            "/": divide
            }
    print(calculator_ascii.logo)
    num1 = float(input("Pick a first number: "))
    for symbol in operations:
        print(symbol)

    next_operation = True
    while next_operation:
        operation_symbol = input("Pick operation: ")
        num2 = float(input("What provide another number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)
        #alternative way print(operations[operation_symbol](num1,num2))

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        continue_answer = ""
        while continue_answer!="y" and continue_answer!="n" and continue_answer!="e":
            continue_answer = input("Do you want to\nContinue with actual answer: y. New calculation: n. Exit: e\n")
            if continue_answer=="y":
                next_operation=True
                num1 = answer
            if continue_answer=="e":
                next_operation=False
            if continue_answer=="n":
                next_operation=False
                calculator()


calculator()