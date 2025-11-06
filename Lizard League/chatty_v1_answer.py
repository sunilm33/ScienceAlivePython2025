def main():
    print("Welcome to Chatty! Here we will talk and learn about eachother.")
    # Create a variable to save the users name
    name = input("What is your name? ")
    print(f"Hello {name}, I'm pleased to meet you!")
    color = input("What is your favourite color? ")
    print(f"Wow {color} sure is neat, I really love it too.")
    print("I can show you a neat trick, give me 2 numbers to multiply together.")
    num1 = input("First number: ")
    num2 = input("Second number: ")
    # print(f"{num1} times {num2} equals {num1*num2}")
    print(f"{num1} times {num2} equals {int(num1)*int(num2)}")
    print("Thanks for chatting with me! I hope to talk to you again soon!")
main()