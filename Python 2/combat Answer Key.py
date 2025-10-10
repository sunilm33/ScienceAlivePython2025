import random
import time

# Global Variables
actions = ["sword", "shield", "bow"]
win = False
max_player_health = 15

# Function to get the winner of a round
# We are going to use rock paper scissors logic to find who wins the round
# Element 0 beats 2
# Element 1 beats 0 
# Element 2 beats 1
def choose_winner(player_choice, enemy_choice):
    print(f"Enemy chose {enemy_choice}!")
    time.sleep(1)
    # Index gets the position in the list (eg. 0,1,2) based on a list element
    action_index_player = actions.index(player_choice)
    # If they both choose the same thing its a tie!
    if player_choice == enemy_choice:
        print("It's a tie!")
        return 0
    # This is tricky part of our logic
    # We want to see if the enemies action is one before in the action list than the player
    elif enemy_choice == actions[action_index_player - 1]:
        print("You won the round!")
        return 1
    # Finally if its not one before or equal to then it has to be the action after which results in a loss
    else:
        print("You lose the round...")
        return -1

# Main Gameplay Area
def main_gameloop():
    # Intro dialogue to setup our game
    print("Welcome to the Python Guild's Dungeon Combat Training")
    print("Here you will choose between Sword, Bow or Shield.")
    print("Sword beats bow, bow beats shield and shield beats sword")
    print("To win a fight be correct 2 out of 3 combats.")
    # Game loop variables
    # continue_game keeps the game looping until someone wins
    # the health variables keep track of how much health is left for each character
    continue_game = True
    current_player_health = max_player_health
    enemy_health = random.randint(10,20)
    # This is what will be returned, True means the player won, False means the enemy won
    win = False
    # Loop to give the player and enemies multiple turns
    while continue_game:
        print(f"Player Health = {current_player_health}, Enemy Health = {enemy_health}")
        print("Next round starts in 3...")
        # Optional to use time.sleep, makes it so each print has a bit of time before being executed
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)

        # Enemy will randomly get an action
        enemy_choice = random.choice(actions)
        # Players have to choose one of the 3 listed actions
        player_choice = input("Are you going to choose sword, shield or bow? ")
        while player_choice not in actions:
            player_choice = input("Please select one of the three actions: sword, shield, bow. ")

        # Use the function choose_winner to get results of the round!
        result = choose_winner(player_choice, enemy_choice)
        time.sleep(1)
        if result == -1:
            current_player_health -= 5
        elif result == 1:
            enemy_health -= 5
        
        # Check healths, if the player is equal to or less than 0 they lose
        # If the enemy is equal or less than 0 the player
        if (enemy_health <= 0 and current_player_health <= 0) or current_player_health <= 0:
            continue_game = False 
        elif enemy_health <= 0:
            win = True
            continue_game = False
    return win

# This will replay the game until a user wants to stop    
while True:
    win = main_gameloop()
    if win:
        print("You won the combat!")
    else:   
        print("You lost the combat...")
    play_again = input("Do you want to play again? ")
    if play_again == "no":
        print("Goodbye! Thank you for playing.")
        break