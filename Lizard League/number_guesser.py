import random
 
def main():
    secret_number = random.randint(0,50)
    
    print("Welcome to the number guessing game.\nI have chosen a secret number. You have 5 guesses to figure it out.")
    guess = int(input("What is your first guess? "))
    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low")
    else:
        print("You guessed it!")
        return
        
    guess = int(input("What is your second guess? "))
    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low")
    else:
        print("You guessed it!")
        
    guess = int(input("What is your third guess? "))
    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low")
    else:
        print("You guessed it!")
        return
        
    guess = int(input("What is your fourth guess? "))
    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low")
    else:
        print("You guessed it!")
        return
    
    guess = int(input("What is your fifth guess? "))
    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low")
    else:
        print("You guessed it!")
        return

    print(f"You didnt guess it! The number was {secret_number}")
    
main()