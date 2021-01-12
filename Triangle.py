# Define Operation Functions.
# Function 1 - Missing Internal Angle.
def internalAngle():
    # Setting unit as a string allows for 1 variable change potential. (True also in other operation functions.)
    units = "Degrees"
    
    # Inputs.
    print("\nFind MISSING ANGLE - Please Enter 2 Angles in a Triangle (" + units + ").")
    ang1 = float(input("-> Enter Angle 1: "))
    ang2 = float(input("-> Enter Angle 2: "))

    # IF Statement checking validity of user input. (If units above is in radians, 180 needs to be changed to 2*Pi)
    if (0 < ang1 < 180 and 0 < ang2 < 180 and (ang1 + ang2) < 180): 
        
        #Calculation (For degrees as units only!)
        missingAng = 180 - ang1 - ang2

        # Output.
        # escape characters, '\n' and '\t', are used for formatting to increase clarity and readability. 
        print("\nOUTPUT:")
        print("\tAngle 1: ", ang1, units)
        print("\tAngle 2: ", ang2, units)
        print("\tMissing Angle: ", round(missingAng, 5), units)

        # Return to Main Menu.
        return shapesTriangle()

    # ELSE to restart Function 1 'internalAngle' if values are invalid.
    else:
        print("Please Enter Valid Angles...")
        return internalAngle()
    return


# Function 2 - Hypotenuse Length.
def hypotenuseLength():
    units = "CM"

    # Inputs. 
    print("\nFind HYPOTENUSE - Please Enter the Length of 2 Sides of a Right Angle Triangle (" + units + ").")
    length1 = float(input("-> Enter Length 1: "))
    length2 = float(input("-> Enter Length 2: "))

    # Calculation - Pythagoras Theroem.
    missingHypotenuse = (length1**2 + length2**2)**0.5

    # Outputs.
    # escape characters, '\n' and '\t', are used for formatting to increase clarity and readability. 
    print("\nOUTPUT:")
    print("\tLength 1: ", length1 , units)
    print("\tLength 2: ", length2, units)

    # 'round()' function used to simplify unmanagble float outputs and account for floating point error, to 2 decimal places.
    print("\tHypotenuse (2 d.p.): ", round(missingHypotenuse, 2), units)

    # Return to Main Menu.
    return shapesTriangle()


# Function 3 - Area.
def triangleArea():
    units = "CM"

    # Inputs
    print("\nFind AREA - Please Enter the Length of 3 Sides of a Traingle (" + units + ").")
    length1 = float(input("-> Enter Length 1: "))
    length2 = float(input("-> Enter Length 2: "))
    length3 = float(input("-> Enter Length 3: "))

    # Calculation - Area given three sides.
    halfPeri = (length1 + length2 + length3)/2    # division means FLOAT with decimal of .5.
    missingArea = (halfPeri*(halfPeri - length1)*(halfPeri - length2)*(halfPeri - length3))**0.5

    # Outputs.
    # escape characters, '\n' and '\t', are used for formatting to increase clarity and readability. 
    print("\nOUTPUT:")
    print("\tLength 1: ", length1, units)
    print("\tLength 2: ", length2, units)
    print("\tLength 3: ", length3, units)

    # 'round()' function used to simplify unmanagable float outputs and account for floating point error , to 2 decimal places.
    print("\tArea (2 d.p.): ", round(missingArea, 2), units + " Squared")

    # Return to Main Menu.
    return shapesTriangle()


# Define over-arching function to select desired operation.
# Funtion can thus be called to return to Main Menu upon completion of each operation (or if invalid input).
def shapesTriangle():
    
    # Main Menu. '\n' Used here to seperate menu from previous output and upcoming operations.
    print("\nMAIN MENU") 
    print("To Find a MISSING INTERNAL ANGLE, Enter 1.")
    print("To Find the HYPOTENUSE LENGTH, Enter 2.")
    print("To Find the AREA, Enter 3.")
    print("To QUIT, Enter q.\n")

    functionSelector = input("-> Enter Desired Operation Selector [1/2/3/q]: ")

    # IF statement to determine desired operation and send user to associated function.
    if (functionSelector == "1"):
        internalAngle()

    elif (functionSelector == "2"):
        hypotenuseLength()

    elif (functionSelector == "3"):
        triangleArea()

    elif (functionSelector == "q"):

        # Quitting Confirmation
        quitQuestion = input("\nYou are about to close the program.\n-> Are you sure? [yes]: ")
        if (quitQuestion == "yes"):
            print("Closing Program...")
            exit()
        else:
            print("Returning to Main Menu...")
            return shapesTriangle()

    # ELSE here used to catch any user input error. Returns user to Main Menu.
    else:
        print("Please enter a valid input...")
        return shapesTriangle()
    return


#Calling function to being Triangle Operations.
shapesTriangle()
