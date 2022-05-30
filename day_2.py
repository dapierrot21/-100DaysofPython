### Python Primitive Data Types ###
# String
print(type("Hello"))

# Intger
print(type(22))

# Float
print(type(3.14159))
print(type(734_529.678)) # The underscore is there to make the large number more readable.

# Boolean
print(type(1 == 1))


# Subscript
# "Hello" -> H[0], e[1], l[2], l[2], 0[3] -> position of each character in string "Hello".

### Type Error, Type Checking and Type Conversion ###
# type() - shows the type of data. See above.

print(type(str(1)))
print(type(int("123")))

# Excerise 1

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆


####################################
#Write your code below this line 👇
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
total_amount = first_digit + second_digit

print(f"{total_amount}")



# Mathematical Operations in Python
# Addition
3 + 5
# Subtraction
5 - 3
# Multipilication
5 * 3
# Division - will always return a float data type
5 / 3 
# Exponents & Power - power defines a base number raised to the exponent, where base number is the factor which is multiplied by itself and exponent denotes the number of times the same base number is multiplied
5 ** 3

# Order of which operations is excuted.
# PEMDAS
# 1. Any with a set of Parentheses. If nested parentheses the inner most one is excuted first.
# 2. Exponents

## Which ever operations that is most to the left will be excuted first because you read math from left to right.
# 3. Multipilication # 4. Division
# 5. Addition # 6. Subtraction

# 1. 3 * 3 = 9 : print(9 + 3 / 3 - 3)
# 2. 3 / 3 = 1.0 : print(9 + 1.0 - 3)
# 3. 9 + 1 = 10.0 : print(10.0 - 3)
# 4. 10 - 3 = 7.0 : print(7.0)
# Output: 7.0
print(3 * 3 + 3 / 3 - 3)


# Excerise 2
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
bmi = int(weight) / (float(height) ** 2) 

print(int(bmi))

# Number Manipulation and F Strings in Python

# Floor Division
print(type(8 // 3))

# F String
score = 0
height = 1.8
isWinning = True

print(f"Your score is {score}, your height is {height}, Did you win? {isWinning}!")


# Exercise 3
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# how many yrs we have left until 90 yrs old.
years = 90 - int(age) 

# Then take that number and multipily 
months = round(years * 12)  # 12(months in a year)
weeks = round(years * 52) # 52(weeks in a year)
days = round(years * 365) # 365(days in a year)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")


# Tip Calculator
print("Welcome to your tip calculator.")

bill_total = float(input("What was the total bill?\n$"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
bill_split = int(input("How many people will split this bill?\n"))

new_per_tip = percentage_tip / 100
bill_total_with_tip = bill_total * new_per_tip
new_bill = bill_total + bill_total_with_tip
bill_per_person = new_bill / bill_split

print("Each person should pay: ${:.2f}".format(round(bill_per_person, 2)))
