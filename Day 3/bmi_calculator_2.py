height = float(input("Enter your height in (m): "))
weight = int(input("Enter your weight in (kg): "))
bmi = (weight / (height ** 2))
round_value = round(bmi)

if round_value < 18.5:
    print(f"Your BMI is {round_value}, you are underweight.")
elif round_value < 25:
    print(f"Your BMI is {round_value}, you have a normal weight.")
elif round_value < 30:
    print(f"Your BMI is {round_value}, you are slightly overweight.")
elif round_value < 35:
    print(f"Your BMI is {round_value}, you are obese.")
else:
    print(f"Your BMI is {round_value}, you are clinically obese.")