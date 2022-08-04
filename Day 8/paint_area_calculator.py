# 1st way -
def paint_calc(height, width):
    coverage = 5
    number_of_cans = (height * width) / coverage
    print(f"You'll need {round(number_of_cans)} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))

paint_calc(height=test_h, width=test_w)

# 2nd way -
import math

def paint_calc(height, width, cover):
    num_cans = (height * width) / cover
    round_up_cans = math.ceil(num_cans)
    print(f"You'll need {round_up_cans} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)