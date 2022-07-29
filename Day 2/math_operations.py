print( 3 + 2)
print(8 - 4)
print(8 * 4)
print(8 / 4)
print(8 ** 2)
print(8 % 4)

# NOTE:-
# Operations are followed in a sequence
# PEMDAS
# ()
# **
# * and /
# + and -

print(3 * 3 + 3 / 3 -3)
print(3 * (3 + 3) / 3 -3)
print(3 * 3 / 3 + 3 -3)

# Round Function
print(round(2.666666666 , 2))
print(round(2.666666666))

# Flow Division (to get output as int) bcous division always gets output as float
print(4 / 2)
print(4 // 2) # --> Flow division
print(type(4 // 2))

result = 4 / 2
result /= 2
print(result)

# We can also use -=, *=, /= etc

# f-Strings (to mix data types)
print("your score is " + str(result)) #--> without fstring
print(f"your score is {result}") #--> with fstring
