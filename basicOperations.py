# SUM Function
def sum(x, y):
    answer = x + y
    return answer


# PRODUCT Function
def prod(x, y):
    # FOR Loop iterating addition of x.
    answer = x
    for _ in range(y-1):
        answer += x
    return answer


# EXPONENTIAL Function
def exp(x, y):
    # FOR Loop iterating previous Product function.
    answer = x
    for _ in range(y-1):
        answer = prod(answer, x)
    return answer


# MODULUS Function
def modulo(x, y):
    # WHILE to iterate addition (of a negative number).
    negy = (-y)
    answer = x
    while (answer >= y):
        answer += negy
    return answer


# Function ensuring positive, non-zero values, with re-entry if neccessary.
def positiveChecker(x, y):
    while (x <= 0 or y <= 0):
        print("\nPlease Enter Positive, Non-Zero Inputs.\n")
        x = float(input("--> Re-Enter Number 1: "))
        y = float(input("--> Re-Enter Number 2: "))
    return x, y


# Define over-arching function to select desired operation. Assuming all input will be of the correct data type.
# Funtion can thus be called to return to Main Menu upon completion of each operation (or if invalid input).
def basicOperations():
    
    # Main Menu. '\n' Used here to seperate menu from previous output and upcoming operations.
    print("\nMAIN MENU") 
    print("To SUM two numbers, Enter 1.")
    print("To MULTIPLY two numbers, Enter 2.")
    print("To find the EXPONENTIAL, Enter 3.")
    print("To find the MODULUS, Enter 4.")
    print("To QUIT, Enter q.\n")

    functionSelector = input("-> Enter Desired Operation Selector [1/2/3/4/q]: ")

    # IF statement to determine desired operation and send user to associated function.
    if (functionSelector == "1"):
        #Input Values
        print("\nSUM - Please input 2 numbers to be added together.")
        add1 = float(input("--> Enter Number 1: "))
        add2 = float(input("--> Enter Number 2: "))

        # Print Answer.
        print("\tANSWER: ", sum(add1, add2))

    elif (functionSelector == "2"):
        #Input Values
        print("\nPRODUCT - Please input a positive number and a positive integer to be multiplied together.")
        mult1 = float(input("--> Enter Number 1: "))
        mult2 = int(input("--> Enter Number 2 (Integer): "))

        # Value Checking
        (mult1, mult2) = positiveChecker(mult1, mult2)

        # Print answer to 5 decimal places (accounts for some floating point error). Recast neccessary values after positiveChecker.
        print("\tANSWER: ", round(prod(mult1, int(mult2)), 5))

    elif (functionSelector == "3"):
        #Input Values
        print("\nEXPONETIAL - Please input 2 positive integers.")
        num = int(input("--> Enter Number 1: "))
        power = int(input("--> Enter Number 2 (Power): "))

        # Value Checking
        (num, power) = positiveChecker(num, power)

        # Print answer. Recast neccessary values after positiveChecker.
        print("\tANSWER: ", exp(int(num), int(power)))

    elif (functionSelector == "4"):
        #Input Values
        print("\nMODULUS - Please input 2 numbers; a numerator, and a denominator.")
        mod1 = float(input("--> Enter Number 1: "))
        mod2 = float(input("--> Enter Number 2: "))

        # Value Checking
        (mod1, mod2) = positiveChecker(mod1, mod2)

        # Print answer to 5 decimal places (accounts for floating point error).
        print("\tANSWER: ", round(modulo(mod1, mod2), 5))

    elif (functionSelector == "q"):
        # Quitting Confirmation
        quitQuestion = input("\nYou are about to close the program.\n-> Are you sure? [yes]: ")
        if (quitQuestion == "yes"):
            print("Closing Program...")
            exit()

        else:
            print("Returning to Main Menu...")

    # ELSE here used to catch any Main Menu user input error. Returns user to Main Menu.
    else:
        print("Please enter a Valid Menu Option...")
    
    return basicOperations()


# Calling Function to begin.
basicOperations()
