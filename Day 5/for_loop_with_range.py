for number in range(1, 10):
    print(number)

for number in range(1, 11, 3): # --> steping number by 3 in the range from 1 to 11 (11 not included)
    print(number)

# Add all numbers from 1 to 100
sum = 0
for num in range(1, 101):
    sum += num
print(f"The sum of all numbers from 1 to 100 is: {sum}")