dialogue_1_options = ["A. Okay,  where do you need help?",
                    "B. No, I don't know how to do that.",
                    "C. How much are you willing to pay me?"]
dialogue_2_options = ["A. That works for me.",
                    "B. No can do, I need at least 5 silver.",
                    "C. Nope, 10 silver or I walk!"]
dialogue_3_options = ["A. Okay 3 it is.",
                      "B. No that is way too low.",
                      "C. Good riddance, I can't do that price."]
def get_input():
    return input("Please input A, B or C and press enter to choose your option. ")

def main():
    # Dialogue Tree
    # Here we are going to demo how to talk and start quests
    accepted_quest = False 
    ask_for_money = False
    monetary_amount = 0
    print(f"Hello Adventurer. I need help with clearing the rats out of my cellar.")
    print(dialogue_1_options[0])
    print(dialogue_1_options[1])
    print(dialogue_1_options[2])
    dialogue_input = get_input()

    if dialogue_input == "A":
        print("In. My. Cellar.\nI can pay you 2 silver to do it.")
        monetary_amount = 2  
        ask_for_money = True
        accepted_quest = True
    elif dialogue_input == "B":
        accepted_quest = False
    elif dialogue_input == "C":
        ask_for_money = True
        print("Oh I dont have too much money, I can pay 3 silver coins.")
        monetary_amount = 3 

    if ask_for_money:
        print(dialogue_2_options[0])
        print(dialogue_2_options[1])
        print(dialogue_2_options[2])
        dialogue_input = get_input()

        if dialogue_input == "A":
            print("Thank you, now please go clear them out!")
            accepted_quest = True
        elif dialogue_input == "B":
            print("Oh well I can use my kids savings and get that money. I really need these rats gone.")
            accepted_quest = True
            monetary_amount = 5
        elif dialogue_input == "C":
            print("I CANNOT AFFORD THAT. Final offer is 3 silver!") 
            print(dialogue_3_options[0])
            print(dialogue_3_options[1])
            print(dialogue_3_options[2])
            dialogue_input = get_input()
            if dialogue_input == "A": 
                print("Okay good, now go help me!")
                monetary_amount = 3
                accepted_quest = True
            elif dialogue_input == "B" or dialogue_input == "C":
                print("Good luck with your life, I'll find a more reasonable person soon enough.")
                accepted_quest = False

    if accepted_quest:
        print("You are helping the townsperson! You got paid " + str(monetary_amount) + " silver coins!")
    else: 
        print("Well you failed to get a quest, you'll have to keep searching now.")
  
# Uncomment the next line to test the program           
main()
        