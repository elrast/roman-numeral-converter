# Converts Roman numerals to integers and vice versa, checking for format.

# Check that Roman numeral has valid format
def isValidRoman(roman):
    # If number is too long, return false
    inputlength = len(roman)
    if inputlength > 5:
        return False

    roman = roman.upper()

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

# Convert Roman numeral to integer
def romToInt():
    convert = str(raw_input("Enter the Roman numeral to convert: "))
    if isValidRoman(convert)
        # do things

# Convert integer to Roman numeral

# Get input to convert
convtype = ""
convtype = raw_input("Enter 'R' to convert a Roman numeral to an integer.\nOr, enter 'I' to convert from an integer to a Roman numeral: ")
if convtype == "R"
    romToInt()
elif convtype == "I"
    intToRom()
else
    print "Invalid choice! Try again."
