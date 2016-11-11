# If user selects 1, then do binary to decimal conversion. Otherwise, if 2 do
# decimal to binary conversion.
def menu(userInput):
    if(userInput == 1):
        binary = raw_input("Enter binary number: ")
        # Convert decimal to binary form
        decimal = binary_to_decimal(binary)
        return decimal

    elif(userInput == 2):
        decimal = raw_input("Enter decimal number: ")
        binary = decimal_to_binary(decimal)
        return binary

# Convert binary number to its decimal by following the formula
# Digit * 2^(Position #)
def binary_to_decimal(num):
    # This puts the digits into a list. Ex. 11 is ['1', '1']
    digit = list(num)
    # This counts the position number so for 11 it will be 2
    position = len(list(num))
    n = position - 1
    decimal = 0
    i = 0 # The ith power
    while(i < position):
        # Start from the last list element
        x = int(digit[n])

        # Check if user input is in binary form.
        if(x < 0 or x > 1):
            print "NOT IN BINARY FORM"
            return None

        result = x * (2**i)
        decimal = decimal + result
        i += 1 # Increase the ith power position
        n -= 1 # Move to left digit of the digit array

    return decimal

def decimal_to_binary(num):
    quot = int(num)
    binary = list() # Create a empty list

    while(quot > 0):
        rem = quot % 2 # Get the remainder
        binary.append(str(rem)) #
        quot = quot // 2

    binary.reverse()
    return int(''.join(binary)) # Convert list to a string then to a int


def welcome():
    print "Binary to Decimal Converter!"
    print "What would you like to convert?\n"
    print "Press 1 for Binary to Decimal."
    print "Press 2 for Decimal to Binary."
    print "Press 3 to EXIT."

    userInput = raw_input("Select: ")
    while(int(userInput) != 3):
        input = menu(int(userInput))
        print "Result : ", input
        userInput = raw_input("Select: ")

welcome()
