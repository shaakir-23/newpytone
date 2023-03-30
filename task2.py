# Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
#  how does an even / odd number react differently when divided by 2?


input_num = int(input('Enter any number: '))

if input_num % 2 == 0:

    print(input_num, "is EVEN")

else:
    
    print(input_num, "is ODD")