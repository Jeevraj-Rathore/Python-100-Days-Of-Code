# Imagine a person lives for 90 years on average

age = int(input("What is your current age? "))
remaining_age = 90 - age
days = remaining_age * 365
weeks = remaining_age * 52
months = remaining_age * 12
print(f"You have {days} days, {weeks} weeks, and {months} months left.")