# Excerise 1
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

# Using \n 'newline'
print("Day 1 - Python Print Function\nThe function is declared like this:\nprint('what to print')")

# Combinig String
print("Hello" + " Dean")

# Excerise 2
# Fix code below
# print(Day 1 - String Manipulation")
# print("String Concatenation is done with the "+" sign.")
#   print('e.g. print("Hello " + "world")')
# print(("New lines can be created with a backslash and n.")

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

# Input function - input(): the input function takes what inside the function "what is your name" and replace it with what the user enters.
name = input("what is your name?")
print(name)

print("Hello " + input("what is your name?"))


# Excerise 3
# input() function replace the string inside with what is type from the user, then that string is counted one characther at a time by the len() which also returns that amount of characthers to print to display.
print(len(input("what is your first name")))



# Excerise 4
# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# The value stored in the a & b variables are switched where the b value is now the value stored in a and the a value is not the value that was stored in the b variable. 
a, b = b, a


#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

# Day 1 final project 

#1. Create a greeting for your program
print("Welcome to Band Name Generator!!!!!")

#2. Ask the user for city that they grew up in.
city = input("What city did you grow up in? \n")

#3. Ask the user for a name of a pet.
pet = input("What is your pet name? \n")

#4. Comebine the city name and pet name to show them their band
# f"" -  allows me to format the string with the values of variables city and pet.
print(f"Your band is The {city} {pet}!")