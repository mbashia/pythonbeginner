# simple rock, paper, scissors game
import random
while True:
    user_action = input("enter choice [rock,paper scissors]:")
    choices = ['rock', 'paper', 'scissors']
    computer_action = random.choice(choices)
    print(f'you chose {user_action} and the computer chose {computer_action}')
    if computer_action == user_action:
        print("you have tied")
    elif computer_action == "rock":
        if user_action == "paper":
            print(" you win !!")
        else:
            print("rock smashes paper.. you lose!!!")
    elif computer_action == "paper":
        if user_action == "scissors":
            print(" you win!!")
        else:
            print("paper covers rock... you lose!!!")
    elif computer_action == "scissors":
        if user_action == "rock":
            print("you win!!")
        else:
            print("scissors cuts paper... you lose!!")
    again = input("would you like to play again[y/n]:")
    if again.lower() == 'n':
        break
    elif again.lower() == "y":
        continue
    else:
        print("invalid choice")
        break