# Converts Roman numerals to integers and vice versa, checking for format.

# Check that Roman numeral has valid format
def isValidRoman(roman):
    # If number is too long, return false
    inputlength = len(roman)

    # Exceeds maximum possible
    if "MMMMM" in roman:
        return False

    # Search for invalid sequences within Roman number
    invalid4combo = ["IIII", "XXXX", "CCCC"]
    for i in xrange(inputlength-3):
        if roman[i:i+4] in invalid4combo:
            return False

    invalid3combo = ["VIV", "VIX", "IXV", "IIV", "IVI", "IIX", "IXI", "IXX",
                     "IXL", "IXC", "XXL", "XLX", "XXC", "XCX", "XCC", "XCD",
                     "XCM", "LXL", "LXC", "XCL", "CCD", "CDC", "CCM", "CMC",
                     "CMM", "DCD", "DCM", "CMD"]
    for i in xrange(inputlength-2):
        if roman[i:i+3] in invalid3combo:
            return False

    invalid2combo = ["VV", "VX", "VL", "VC", "VD", "VM", "IL", "IC", "ID",
                     "IM", "XD", "XM", "LL", "LC", "LD", "DD", "DM"]
    for i in xrange(inputlength-1):
        if roman[i:i+2] in invalid2combo:
            return False

    # Else, return true
    return True



# Convert Roman numeral to integer
def romToInt():
    roman = str(raw_input("Enter the Roman numeral to convert: "))
    roman = roman.upper()
    if not isValidRoman(roman):
        return "Invalid Roman numeral"
    else:
        romanValues = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        numeric = 0
        for digit in roman:
            if digit in romanValues:
                numeric += romanValues[digit]
            else:
                return "Invalid letter in Roman numeral"
        # Correct initial calculation
        if "IV" in roman:
            numeric -= 2
        if "IX" in roman:
            numeric -= 2
        if "XL" in roman:
            numeric -= 20
        if "XC" in roman:
            numeric -= 20
        if "CD" in roman:
            numeric -= 200
        if "CM" in roman:
            numeric -= 200

        return numeric



# Convert integer to Roman numeral
def intToRom():
    numeral = ""
    integer = raw_input("Enter the integer to convert: ")
    value = int(integer)

    if value >= 5000 or value < 1:
        return "Invalid integer input"

    while len(integer) < 4:
        integer = "0" + integer

    thousands = int(integer[0])
    hundreds = int(integer[1])
    tens = int(integer[2])
    ones = int(integer[3])

    if thousands < 1:
        pass
    else:
        numeral += "M" * thousands

    if hundreds < 4:
        numeral += "C" * hundreds
    elif hundreds == 4:
        numeral += "CD"
    elif hundreds < 9:
        numeral += "D" + "C" * (hundreds-5)
    elif hundreds == 9:
        numeral += "CM"
    else:
        pass

    if tens < 4:
        numeral += "X" * tens
    elif tens == 4:
        numeral += "XL"
    elif tens < 9:
        numeral += "L" + "X" * (tens-5)
    elif tens == 9:
        numeral += "XC"
    else:
        pass

    if ones < 4:
        numeral += "I" * ones
    elif ones == 4:
        numeral += "IV"
    elif ones < 9:
        numeral += "X" + "I" * (ones-5)
    elif ones == 9:
        numeral += "IX"
    else:
        pass

    return numeral


# Print welcome message
def intro():
    print "===== Welcome to the Roman numeral converter! ====="

# Get input to convert
def main():
    convtype = ""
    convtype = raw_input("A) Roman numeral --> integer\nB) Integer --> Roman numeral\n")
    if convtype == "A" or convtype == "a":
        print romToInt()
    elif convtype == "B" or convtype == "b":
        print intToRom()
    else:
        print "Invalid choice! Try again."
    keepgoing = raw_input("Do you want to try again? Y/N: ")
    if keepgoing == "Y" or keepgoing == "y":
        main()
    else:
        print "Thank you for playing!"
        raw_input("> Hit enter to close window")


if __name__ == "__main__":
    intro()
    main()
