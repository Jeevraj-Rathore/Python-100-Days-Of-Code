def format_name():
    first_name = input("What is your first name?: ")
    surname = input("What is your surname?: ")
    if first_name == "" or surname == "":
        return print("Please provide valid inputs.")
    full_name = (first_name + " " + surname).title()
    return print(full_name)

format_name()