# Function with more than 1 input -
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Jeevraj", "Jaipur") # ==> It's an positional argument (parameter and argument positions must be checked) becouse order matters

greet_with(location="Jaipur", name="Jeevraj") # ==> It's an keyword argument order doesn't matter