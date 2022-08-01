sum = 0
for num in range(2, 101, 2):
    sum += num
print(f"The sum of all numbers from 1 to 100 is: {sum}")

sum2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        sum2 += number
print(f"The sum of all numbers from 1 to 100 is: {sum}")