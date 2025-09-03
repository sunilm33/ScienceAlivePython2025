import random
import time

# Player Actions
# Attack, attempt an attack that might miss
# Heal, regain 10 hp

## GLOBAL VARIABLES
enemy_list = ["goblin", "rhino", "rat", "giant rat who makes all the rules", "shinkenger", "dekaranger", "doggie cruger"]    
enemy_name = ""
enemy_health = 5
enemy_damage_lower = 5
enemy_damage_upper = 10
enemy_defence = 10

player_hp_max = 15
player_hp_current = player_hp_max
player_damage = 5
player_defence = 10
player_heal = 10

## Action Functions

# Generic Attack
def attack(hp, damage, defence):
    hit_attempt = random.randint(0,10)
    if hit_attempt <= defence:
        damage = 0
    hp = hp - damage
    return hp, damage
# Player Attack
def player_attack(hp):
    hp_left, damage_done = attack(hp, player_damage)
    if damage_done > 0:
        print(f"You hit the enemy for {damage_done} damage.")
    else:
        print("Your attack missed!")
    return hp_left

# Enemy Attack
def enemy_attack(hp):
    enemy_damage = random.randint(enemy_damage_lower, enemy_damage_upper)
    hp_left, damage_done = attack(hp, enemy_damage)
    if damage_done > 0:
        print(f"You got hit! {enemy_damage} damage taken.")
    else:
        print("You dodged the attack!")
    return hp_left

def main():
    continue_game = True
    enemy_name = random.choice(enemy_list)
    while continue_game:
        player_name = input("Welcome, what is your name? ")
        print(f"Welcome {player_name} to The Python Guild's Practice Dungeon. \nHere you will take on many monsters in order to train for the real thing. \nTime to enter the dungeon\n")
        time.sleep(1)
        print(f"A {enemy_name} appears!")

# def main():
#     print("Welcome to fighting spirit! You will face a new enemy on each wave.")
#     continue_game = True
#     while continue_game:
#         entry = input("Do you want to enter?")
#         if entry == "No":
#             continue_game = False
#             break
#         enemy_name = random.choice(enemy_list)
#         enemy_health = random.randint(5,20)
#         enemy_damage = random.randint(enemy_damage_lower, enemy_damage_upper)
#         print(f"You turn into a room and see a {enemy_name}.")
#         print(f"They have {enemy_health}hp and {enemy_defence} defence.")
#         while enemy_health > 0:
#             input("Press enter to try an attack..")
#             print("You attack...")
#             attack_roll = random.randint(1,20)
#             time.sleep(1)
#             if attack_roll >= enemy_defence:
#                 enemy_health = enemy_health - player_damage
#                 print(f"You hit for {player_damage} damage! {enemy_name} has {enemy_health} health.")
#             else:
#                 print("You missed!")
#             time.sleep(1)
#             print(f"Time for the enemy's attack...")
#             time.sleep(1)
#             enemy_attack_roll = random.randint(1,20)
#             if enemy_attack_roll >= defence:
#                 player_hp_max = player_hp_max - enemy_damage
#                 print(f"You got hit and now have {player_hp_max}.")
#             else:
#                 print("They missed!")
#             if player_hp_max <= 0:
#                 print("You lost and have to retreat out of the dungeon.")
#                 break
#     return

main()