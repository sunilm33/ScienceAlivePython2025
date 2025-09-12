import random
import time

# Global Variables
actions = ["sword", "shield", "bow"]
win = False
max_p_health = 15
p_damage = 5
# Function to get the winner of a round

def choose_winner(player_choice, enemy_choice):
    print(f"Enemy chose {enemy_choice}!")
    time.sleep(1)
    action_index_p = actions.index(player_choice)
    if player_choice == enemy_choice:
        print("It's a tie!")
        return 0
    elif enemy_choice == actions[action_index_p - 1]:
        print("You won the round!")
        return 1
    else:
        print("You lose the round...")
        return -1

# Main Gameplay Area
def main():
    print("Welcome to the Python Guild's Dungeon Combat Training")
    print("Here you will choose between Sword, Bow or Shield.")
    print("Sword beats bow, bow beats shield and shield beats sword")
    print("To win a fight be correct 2 out of 3 combats.")
    continue_game = True
    current_p_health = max_p_health
    enemy_health = random.randint(10,20)
    e_damage = random.randint(1,p_damage)
    win = False
    while continue_game:
        print(f"Player Health = {current_p_health}, Enemy Health = {enemy_health}")
        print("Next round starts in 3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        enemy_choice = random.choice(actions)

        player_choice = input("Are you going to choose sword, shield or bow? ")
        while player_choice not in actions:
            player_choice = input("Please select one of the three actions: sword, shield, bow. ")

        result = choose_winner(player_choice, enemy_choice)
        time.sleep(1)
        if result == -1:
            current_p_health -= e_damage
        elif result == 1:
            enemy_health -= p_damage

        if (enemy_health <= 0 and current_p_health <= 0) or current_p_health <= 0:
            continue_game = False 
        elif enemy_health <= 0:
            win = True
            continue_game = False
    return win

# This will replay the game until a user wants to stop    
while True:
    win = main()
    if win:
        print("You won the combat!")
    else:   
        print("You lost the combat...")
    play_again = input("Do you want to play again? ")
    if play_again == "no":
        print("Goodbye! Thank you for playing.")
        break
    else:
        while True:
            choice = input("Would you like to upgrade health or attack? ")
            if choice.lower() == "health":
                max_p_health += 2
                break
            elif choice.lower() == "attack":
                p_damage += 2
                break