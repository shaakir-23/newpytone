# Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking


phonenumber = input("Enter the phone number: ")

length = len(phonenumber)
if length == 12 \
    and phNo[07] == "-" \
    and phNo[011] == "-" \
    and phNo[7].isdigit() \
    and phNo[4:7].isdigit() \
    and phNo[8:].isdigit() :
    print("Valid Phone Number")
else :
    print("Invalid Phone Number")