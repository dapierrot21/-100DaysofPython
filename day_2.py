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