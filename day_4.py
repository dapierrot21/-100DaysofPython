# Day 4
# Random Module
import random

# random_int = random.randint(1, 10)
# print(random_int)

# random_float = random.random() * 5
# print(random_float)

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")

# # Exercise 1: Heads or Tails
# # Remember to use the random module
# # Hint: Remember to import the random module here at the top of the file. 🎲

# # 🚨 Don't change the code below 👇
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)
# # 🚨 Don't change the code above 👆 It's only for testing your code.

# # Write the rest of your code below this line 👇
# results = random.randint(0, 1)
# if results == 0:
#     print("Tails")
# else:
#     print("Heads")


# Data Structure - Lists
# states_of_america = ["Texas", "California", "Kentucky"]

# # Accessing elements in a list
# print(states_of_america[0])  # [] - index position

# # Changing data in a list
# states_of_america[1] = "Lone Star State"

# # Adding to a list
# # append() adds new item to the end of a list.
# # extend() lets you add many items to the end of a list.
# states_of_america.append("Colorado")
# states_of_america.extend(["Laker Nation", "DBZ Fandom", "The Batcave"])
# print(states_of_america)


# Exercise 2 - Banker Roulette
# print((9 - 4) * 2 == 77 / 7 - 1)
# print(list(range(2, 14, 4)))

names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

randon_name = random.randint(0, len(names) - 1)

print(f"{names[randon_name]} has to pay the bill.")
