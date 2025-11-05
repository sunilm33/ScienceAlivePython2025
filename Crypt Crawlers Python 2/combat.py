import random
import time

# Global Variables

# Function to get the winner of a round
# We are going to use rock paper scissors logic to find who wins the round
# Element 0 beats 2
# Element 1 beats 0 
# Element 2 beats 1
def choose_winner(player_choice, enemy_choice):
    return 

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

    
    # Loop to give the player and enemies multiple turns

        # Print out health of player and enemy.

        # Start a round timer
        # Optional to use time.sleep, makes it so each print has a bit of time before being executed
        
        # Enemy will randomly get an action using random.choice()

        # Players have to choose one of the 3 listed actions
        
        # Use the function choose_winner to get results of the round!
        

        # Check healths, if the player is equal to or less than 0 they lose
        # If the enemy is equal or less than 0 the player
        
    return

# Everything below this will execute right when we start up
# A While True loop is used to continue playing the game until the player wants to stop   
while True:
    # Call the main game loop

    # Display a message if the player wins

    # Asks if the player wants to play again

    # Break stops a loop, we will use this to stop infinite loops 
    break