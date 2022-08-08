# enemies = 1

# def increse_enemies():
#     enemies = 2
#     print(f"Enemies inside function: {enemies}")

# increse_enemies()
# print(f"Enemies inside function: {enemies}")

# Local Scope --> It exists within functions and can't be called outside the function
# def drink_portion():
#     portion_strenght = 2
#     print(portion_strenght)

# drink_portion()

# Global Scope --> Can be accessed from anywhere
# player_health = 10

# def drink_portion():
#     portion_strenght = 2
#     print(player_health)

# drink_portion()

# There is no such thing like block scope in python
# game_level = 3
# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0] # --> it is a local variable

#     print(new_enemy)

# Modifying Global Scope -
enemies = 1

def increse_enemies():
    # global enemies
    # enemies += 1
    print(f"Enemies inside function: {enemies}")

increse_enemies()
print(f"Enemies inside function: {enemies}")

# NOTE: -
# Don't use same name for local and global variables it's not a good practice
# Don't modify global vaiable within a function that has local scope
# But if you still want to use modified value use return to modify and return the value
# Global scope is usefull when you want to define constants

# Global Constants - (Always use uppercase letters to define such )
PI = 3.14159
URL = "https://www.google.com"
GITHUB_HANDLE = "Jeevraj-Rathore"