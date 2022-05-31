# Control Flow with if/else and Conditional Operators

# > greater than
# < less than
# == equal to
# != not equal to

# Exercise 1 - Even or Odd
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")


# Nested if statements and elif statements
# Multiple If Statements in Succession
print("Welcome to the rollercoaster!")
height = float(input("What is your height in cm?\n"))

# If the height is tall enough.
if height >= 120:
    # then excute this block of code.
    print("You can ride. Enjoy!")
    age = int(input("How old are you?\n"))
    if age >= 18:
        photo = input("Do you want to purchase photos with your ticket? Yes or No\n").lower()
        if photo == 'yes':
            total_cost = 12 + 3
            print(f"Your total amount to pay is {total_cost}.")
        else:
            print("You need to pay $12.")
    elif age <= 18:
        photo = input("Do you want to purchase photos with your ticket? Yes or No\n").lower()
        if photo == 'yes':
            total_cost = 7 + 3
            print(f"Your total amount to pay is {total_cost}.")
        else:
            print("You will need to pay $7.")
    elif age < 12:
        photo = input("Do you want to purchase photos with your ticket? Yes or No\n").lower()
        if photo == 'yes':
            total_cost = 5 + 3
            print(f"Your total amount to pay is {total_cost}.")
        else:
            print("You will need to pay $5.")
    elif age >= 45 and age <= 55:  # Logical Operators
        photo = input( "Do you want to purchase photos? Yes or No\n").lower()
        if photo == 'yes':
            total_cost = 3
            print(f"Your total amount to pay is {total_cost}.")
        else:
            print("Your ticket is free.")
    else:
        print("Your to young to be here buddy.")
else:
    # if the height is not tall enough then excute this code.s
    print("You can't ride.")


# Exercise 2 - BMI 2.0
# # 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(int(weight) / (float(height) ** 2))

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")




# Exercise 3 - Leap Year
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")


# Exercise 3 - Pizza Order
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").lower()
add_pepperoni = input("Do you want pepperoni? Y or N ").lower()
extra_cheese = input("Do you want extra cheese? Y or N ").lower()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total = 0

if size == 's':
    total += 15
elif size == 'm':
    total += 20
else:
    total += 25

if add_pepperoni == 'y':
    total += 3

if extra_cheese == 'y':
    total += 1

print(f"Your final bill is: ${total}.")


# Exercise 4 - Love Calculator
# 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

one_long_string = name1 + name2
one_long_lowercase_string = one_long_string.lower()


t = one_long_lowercase_string.count("t")
r = one_long_lowercase_string.count("r")
u = one_long_lowercase_string.count("u")
e = one_long_lowercase_string.count("e")
first_digit = t + r + u + e


l = one_long_lowercase_string.count("l")
o = one_long_lowercase_string.count("o")
v = one_long_lowercase_string.count("v")
e = one_long_lowercase_string.count("e")
second_digit = l + o + v + e


total_love = int(str(first_digit) + str(second_digit))

if (total_love) < 10 or (total_love) > 90:
    print(f"Your score is {total_love}, you go together like coke and mentos.")
elif (total_love) >= 40 and (total_love <= 50):
    print(f"Your score is {total_love}, you are alright together.")
else:
    print(f"Your score is {total_love}.")


# Treasure Island
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right".').lower()

if choice1 == 'left':
    left = input('You come to a lake. There is a island in the middle of the lake. Type "wait" for a boat. Type "swim" to swim across.').lower()
    if left == 'wait':
        wait = input('You arrive at the island unharmed. There is a house with 3 doors. One "red", one "yellow", and one "blue". Which color do you choose?').lower()
        if wait == 'red':
            print("You enter the room with a guy pointing a ray gun at you. ZAP!. Game Over! ")
        elif wait == 'yellow':
            print("You enter the room and its so bright with shiny gold coins. YOU FOUND THE TREASURE!!!!. You Won!!!!")
        elif wait == 'blue':
            print("You enter a room of your worst nigthmares. Game Over!")
        else:
            print("Sorry that color sent you to a gate way to the sun. Game Over!")
elif choice1 == 'right':
    pill = input('You enter the matrix. Choose a pill a "red" or "blue"').lower()
    if pill == 'red':
        print("Embrace the sometimes painful truth of reality. Your free now.")
    elif pill == 'blue':
        print("Remain in the blissful ignorance of illusion.")
    else:
        print("Your trapped in a void.")
else:
    print("Wrong choice. You will be sent back to the fortnite.")

