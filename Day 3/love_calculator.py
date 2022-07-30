print("Welcome to Love Calculator!")
name1 = input("What is your name?\n").lower()
name2 = input("What is their name?\n").lower()

combained_string = name1 + name2

t = combained_string.count("t")
r = combained_string.count("r")
u = combained_string.count("u")
e = combained_string.count("e")
true = t+r+u+e

l = combained_string.count("l")
o = combained_string.count("o")
v = combained_string.count("v")
e = combained_string.count("e")
love = l+o+v+e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")