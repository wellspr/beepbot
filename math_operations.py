def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def mod(a, b):
    return a % b

def get_input():
    input1 = input("    First number... > ")
    input2 = input("    Second number... > ")
    number1 = int(input1)
    number2 = int(input2)
    return [number1, number2]

def operate(operation, numbers):
    if operation == 0:
        return [add(numbers[0], numbers[1]), " + "]
    elif operation == 1:
        return [subtract(numbers[0], numbers[1]), " - "]
    elif operation == 2:
        return [multiply(numbers[0], numbers[1]), " x "]
    elif operation == 3:
        return [divide(numbers[0], numbers[1]), " / "]
    elif operation == 4:
        return [mod(numbers[0], numbers[1]), " % "]

def execute(operation):
    operations = ["addition", "subtraction", "multiplication", "division", "remainder"]

    operation_index = operations.index(operation)
    numbers = get_input()
    result = operate(operation_index, numbers)
    output_result = str(result[0])
    output_symbol = result[1]

    print("")
    print("    Result: " + str(numbers[0]) + output_symbol + str(numbers[1]) + " = " + output_result)
    print("")

def total(n):
    total = 0
    for item in range(n):
        number = input("Enter number > ")
        number = float(number)
        total = total + number
    return total

def average(n):
    ave = 0
    for item in range(n):
        item = input("Enter number > ")
        number = float(item)
        ave = ave + number
    ave = ave / n
    return ave
