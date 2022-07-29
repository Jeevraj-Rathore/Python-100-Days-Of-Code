# Data Types

# 1. String
print("Hello"[0])

# 2. Integer
print(123 + 345)

# Way to write large integers
print(123_456_789)

# 3. Float
print(3.4562)

# 4. Boolean
print(True)
print(False)

# Use type() to check the type of the variable

# Type Casting (changes one datatype tp another)

num_char = len(input("What is your name? "))
# Default datatype of num_char is int
# String can only be concatenated with a string only
# So change the datatype from int to str
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

a = float(123)
print(type(a))

print(70 + float("100.5"))
print("70" + "100")
print(str(70) + str(100))

# Question : Take input of two digit number and add them and show he output
num = (input("Type a two digit number: "))
print(int(num[0]) + int(num[1]))
