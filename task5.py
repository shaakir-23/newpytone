# Using Python or PHP or Java or Ruby or JavaScript
# # Implement a program that takes 3 form inputs or from the terminal, and stores them in three variables. Return the largest of the three.


num1 = 10
num2 = 14
num3 = 12



if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)