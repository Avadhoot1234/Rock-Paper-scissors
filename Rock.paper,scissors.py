import random
print("Let's paly Rock, Paper and scissors")
user_win=0
computer_win=0
options=["rock","paper","scissors"]

while True:
    user_input=input("Type Rock/Paper/scissors or 'q' to quit ").lower()
    if user_input=="q":
        break
    if user_input not in options:
        continue
    
    random_number=random.randint(0,2)
    computer_guess=options[random_number]
    print("Computer picked:",computer_guess)
    
    if user_input=="rock" and computer_guess=="scissor":
        print("You won!")
        user_win+=1
    elif user_input=="sicissor" and computer_guess=="paper":
        print("You won!")
        user_win+=1
    elif user_input=="paper" and computer_guess=="rock":
        print("You won!")
        user_win+=1
    else:
        print("Computer wins!")
        computer_win+=1

print("Your score is",user_win)