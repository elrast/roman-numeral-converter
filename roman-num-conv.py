# Converts Roman numerals to integers and vice versa, checking for format.

# Check that Roman numeral has valid format
def isValidRoman(roman):
    inputlength = len(roman)
    if inputlength > 5
        return False
    # check for other invalid formats

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
