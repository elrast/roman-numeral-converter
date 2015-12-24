# Converts Roman numerals to integers and vice versa, checking for format.

# Check that Roman numeral has valid format
def isValidRoman(roman):
    # If number is too long, return false
    inputlength = len(roman)
    if inputlength > 5:
        return False

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
                     "IM", "XD", "XM", "LL", "LC", "LD", "LD", "DD", "DM"]
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
    integer = int(raw_input("Enter the integer to convert: "))
    if integer >= 5000 or integer < 1
        return "Invalid integer input"
    # do things

# Get input to convert
convtype = ""
convtype = raw_input("Enter 'R' to convert a Roman numeral to an integer.\nOr, enter 'I' to convert from an integer to a Roman numeral: ")
if convtype == "R"
    romToInt()
elif convtype == "I"
    intToRom()
else
    print "Invalid choice! Try again."
