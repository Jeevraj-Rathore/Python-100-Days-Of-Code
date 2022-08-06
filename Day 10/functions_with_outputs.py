# Functions with Outous -
def format_name():
    first_name = input("What is your first name?: ")
    surname = input("What is your surname?: ")
    full_name = (first_name + " " + surname).title()
    return print(full_name)

format_name()