# Bot greetings

def greeting():
    print("Hi! I am Beebot, your personal bot.")

# Functions list
functions = [
    "Simple Calculator",
    "Number of Seconds",
    "Statistics",
    "Create a List",
    "Play Games"
    ]

# Open calculator
def calculator():
    import math_operations

    # List of operations
    operations = ["Add", "Subtract", "Multiply", "Divide", "Remainder"]

    # List all operations to user
    display_list(operations)

    # Record user's choice
    operation = input("Choose an operation: ")

    # Hit 'q' to quit
    while operation != "q":

        if operation == "1":
            print("Addition - Please inform two numbers...")
            math_operations.execute("addition")

        elif operation == "2":
            print("Subtraction - Please inform two numbers... ")
            math_operations.execute("subtraction")

        elif operation == "3":
            print("Multiplication - Please inform two numbers...")
            math_operations.execute("product")

        elif operation == "4":
            print("Division - Please inform two numbers...")
            math_operations.execute("division")

        elif operation == "5":
            print("Remainder - Please inform two numbers...")
            math_operations.execute("remainder")

        operation = input("New operation 1 - Add | 2 - Subtract | 3 - Multiply | 4 - Divide | 5 - Remainder | q - Quit Calculator > ")

# Number of seconds
def number_of_seconds():

    print("Calculate the number of seconds in a given number of years")

    give_it_a_try = input("1 - Continue | 2 - Exit > ")

    while give_it_a_try == "1":

        user_input = input("Enter a (whole) number... ")
        number_of_years = int(user_input)
        number_of_seconds = number_of_years * 365 * 24 * 60 * 60
        output = str(number_of_seconds)

        print("The period of " + user_input + " year(s) have " + output + " seconds!")

        give_it_a_try = input("1 - New Calculation | 2 - Exit > ")


# Calculate averages
def statistics():
    import math_operations

    option = input("1 - Total | 2 - Average | q - Exit > ")

    while option != "q":

        if option == "1" or option == "total":

            items_number = input("How many numbers do you want to sum up ? > ")
            items_number = int(items_number)
            total = math_operations.total(items_number)
            output = str(total)
            print("The total is " + output)

        elif option == "2" or option == "average":

            items_number = input("How many numbers do you want to average over? > ")
            items_number = int(items_number)
            ave = math_operations.average(items_number)
            output = str(ave)
            print("The average is " + output)

        option = input("1 - Total | 2 - Average | q - Exit > ")


# Create and display a list
def create_list():
    import list
    my_list = list.create()
    return my_list

def display_list(my_list):
    import list
    list.display(my_list)
# -->
# Ideas: Make some stuff with the list,
# create a to-do-list, etc


# Play a game
def games():
    import games
    play = input("At the moment I have only a guessing game... Play Game? 1 - Continue | 2 Quit")

    while play != "2":
        games.guess()
        play = input("Play Again? 1 - Yes | 2 - Quit")
# -->
# Create new games

# Select something to do
def do_something(option):
    # Calculator
    if option == "1":
        calculator()

    # Number of seconds
    elif option == "2":
        number_of_seconds()

    # Calculate Average
    elif option == "3":
        statistics()

    # Create a List
    elif option == "4":
        list = create_list()
        display_list(list)

    # Play Games
    elif option == "5":
        games()


def run():
    import bot_images

    # Say Hello, presents itself and show options
    instructions = ["Is there something I can help?", "1 - Continue | 2 - Quit"]
    bot_images.say(instructions)

    active = input("Type your option here: > ")

    while active == "1":

        # List functionalities to user
        display_list(functions)

        # Record option from user
        option = input("Choose a function from the list: > ")

        #Select something to do
        do_something(option)

        active = input("1 - New function | 2 - Quit > ")

    # Exit program
    print("Ok, Good Bye! Turning off...")
