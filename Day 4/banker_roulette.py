import random

people = input("Give me everybody's names, seperated by a comma. ")
names = people.split(", ") # --> To store input in form of a list

random_num = (random.randint(0, len(names) - 1))
print(f"{names[random_num]} is going to buy the meal today!")

# Easy way is to use random.choice(names) to pick the random person