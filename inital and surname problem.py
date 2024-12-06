# program to make both variables upper case and make the initial
def FormatName(firstName, lastName):
    firstInitial = firstName[0]
    fullName = firstInitial +' '+lastName
    return fullName.upper()


# main program
firstName = input("Please enter your first name here: ")
lastName = input("Please enter your last name here: ")
print(FormatName(firstName, lastName))





