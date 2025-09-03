import random
import time

# Global Variables
actions = ["sword", "shield", "bow"]
win = False

# Function to get the winner of a round

# def choose_winner(player_choice, enemy_choice):
#     print(f"Enemy chose {enemy_choice}")
#     time.sleep(1)
#     if player_choice == enemy_choice:
#         print("It's a tie!")
#         return 0
#     elif (player_choice == actions[0] and enemy_choice == actions[2]) or \
#         (player_choice == actions[1] and enemy_choice == actions[0]) or \
#         (player_choice == actions[2] and enemy_choice == actions[1]):
#         print("You win the round!")
#         return 1
#     else:
#         print("You lose the round...")
#         return -1

def choose_winner(player_choice, enemy_choice):
    print(f"Enemy chose {enemy_choice}")
    time.sleep(1)
    action_index_p = actions.index(player_choice)
    if player_choice == enemy_choice:
        print("It's a tie!")
        return 0
    elif enemy_choice == actions[action_index_p - 1]:
        return 1
    else:
        print("You lose the round...")
        return -1

def main():
    print("Welcome to the Python Guild's Dungeon Combat Training")
    print("Here you will choose between Sword, Bow or Shield.")
    print("Sword beats bow, bow beats shield and shield beats sword")
    print("To win a fight be correct 2 out of 3 combats.")
    continue_game = True
    player_wins = 0
    enemy_wins = 0
    win = False
    while continue_game:

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
        
        if result > 0:
            player_wins += 1
        elif result < 0:
            enemy_wins += 1

        if enemy_wins >= 2:
            continue_game = False
        elif player_wins >= 2:
            win = True
            continue_game = False
    
while True:
    main()
    if win:
        print("You won the combat!")
    else:   
        print("You lost the combat...")
    play_again = input("Do you want to play again? ")
    if play_again == "no":
        print("Goodbye! Thank you for playing.")
        break