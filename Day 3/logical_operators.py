print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride!")
    age = int(input("Please tell us your age: "))
    photo = input("Do you want photo? say yes or no: ")
    photo_charge = 3
    if photo == "yes":
        if age < 12:
            print(f"You have to pay ${5 + photo_charge}")
        elif age <= 18:
            print(f"You have to pay ${7 + photo_charge}")
        elif age >= 45 and age <= 55:
            print(f"Everything is going to be ok. You have to pay only ${photo_charge}")
        else:
            print(f"You have to pay ${12 + photo_charge}")
    else:
        if age < 12:
            print("You have to pay $5")
        elif age <= 18:
            print("You have to pay $7")
        elif age >= 45 and age <= 55:
            print(f"Everything is going to be ok. You have a free ride on us!")
        else:
            print("You have to pay $12")
else:
    print("Sorry you can't ride")