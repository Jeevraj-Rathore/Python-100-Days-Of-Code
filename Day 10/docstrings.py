# docstring -> It is used for multi-line comments and shows up when we call our functions
def format_name():
    """Take a first and last name and format it to return the title case version of the
    name"""
    first_name = input("What is your first name?: ")
    surname = input("What is your surname?: ")
    full_name = (first_name + " " + surname).title()
    return print(full_name)

format_name()