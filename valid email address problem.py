# validation of the email
def emailCheck(email):
    atSign = email.find('@')
    dot = email.find('.')
    if dot == -1 or atSign == -1:
        print("Your email is invalid.")
    else:
        print("Your email is valid.")


# main program
email = input("Please enter your email address here: ")
print(emailCheck(email))