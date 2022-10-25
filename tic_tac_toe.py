import os
import time

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
# initial variables
game_running = True
mark = ''
player = 1
win = ''


def display_board():

    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# check if the position in the board is filled
def check_position(x):
    if board[x] == "-":
        return True
    else:
        return False


# check win :rows.columns and diagnols respectively
def check_win():
    global game_running
    global win
    if board[0] == board[2] == board[3] != "-":
        game_running = False
        win = True
    elif board[3] == board[4] == board[5] != "-":
        game_running = False
        win = True
    elif board[6] == board[7] == board[8] != "-":
        game_running = False
        win = True
    elif board[0] == board[3] == board[6] != "-":
        game_running = False
        win = True
    elif board[1] == board[2] == board[4] != "-":
        game_running = False
        win = True
    elif board[2] == board[5] == board[8] != "-":
        game_running = False
        win = True
    elif board[0] == board[4] == board[8] != "-":
        game_running = False
        win = True
    elif board[2] == board[4] == board[6] != "-":
        game_running = False
        win = True
    elif "-" not in board:
        game_running = False
        print("that's a tie!!")


def play_game():
    global player
    global game_running
    global mark
    display_board()
    while game_running:
        os.system("cls")
        # flip player
        if player % 2 != 0:
            print("player one's chance [X]")
            mark = 'x'
        else:
            print("second players chance [O]")
            mark = 'o'
        number = int(input("enter a number between 1-9: "))

        number -= 1
        # if position has been filled
        while not check_position(number):
            print("you have already entered that number")
            number = int(input("enter number between 1-9:"))

            number -= 1
            check_position(number)


        board[number] = mark
        print(" ")
        display_board()
        check_win()
        # declare winner
        if win:
            if player % 2 != 0:
                print("player one won!!")
            else:
                print("player 2 won!!!")

        player += 1


print("Tic-Tac-Toe Game ~mbashia~")
print("Player 1 [X] --- Player 2 [O]")
print()
print("Please Wait...")
time.sleep(3)
play_game()






