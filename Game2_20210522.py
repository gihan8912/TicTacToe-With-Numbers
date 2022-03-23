# Name: Gihan Ashraf Fekry Mohamed
# ID: 20210522
# Game 2: Tic Tac Toe with numbers


#  first, I made some lists and imported modules that helped me develop the code
import random
list1 = [1, 3, 5, 7, 9]
list2 = [0, 2, 4, 6, 8]
list5 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# determining the number of players
number = int(input("Enter the number of players: "))
while (number > 2) and (number < 0):
    number = int(input("Sorry! This is a single or multiplayer game. Please enter the correct number of players: "))


# printing the game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


def print_board(board):
    print(board[0], "|", board[1], "|", board[2])
    print("----------")
    print(board[3], "|", board[4], "|", board[5])
    print("----------")
    print(board[6], "|", board[7], "|", board[8])


# checking the end of the game
def check_tie(board):
    if "-" not in board:
        print_board(board)
        print("It's a tie! ")
        exit()


# switching the players' turns and taking their inputs
def players(player):
    for player in [1, 2]:
        if player == 1:
            if number == 1:    # this is the case for when there is only 1 player against the pc
                inp = random.choice(list1)
                list1.remove(inp)
                u = True
                i = 0
                while u:
                    inp_position = random.choice(list5)
                    if (inp_position >= 1) and (inp_position <= 9) and (inp_position != 0) and(board[inp_position - 1] == "-"):
                        board[inp_position - 1] = inp
                        print_board(board)
                        u = False
            else:

                x = True
                while x:
                    inp = int(input("Player " + str(player) + ", enter a number from: " + str(list1)))
                    if (inp >= 1) and (inp <= 9) and (inp % 2 != 0) and (inp in list1):
                        inp = inp
                        list1.remove(inp)
                        x = False
                    else:
                        print("Oops! Please enter valid number: ")
                z = True
                while z:
                    inp_position = int(input("Enter the position (positions are from 1 through 9): "))
                    if (inp_position >= 1) and (inp_position <= 9) and (inp_position != 0) and (
                            board[inp_position - 1] == "-"):
                        board[inp_position - 1] = inp
                        print_board(board)
                        z = False
                    else:
                        print("This position is unavailable. please enter another position: ")

        if player == 2:    # This is the case for when there are 2 users playing together
            y = True
            while y:
                inp = int(input("Player " + str(player) + ", enter a number from: " + str(list2)))
                if (inp >= 0) and (inp <= 9) and (inp % 2 == 0) and (inp in list2):
                    inp = inp
                    list2.remove(inp)
                    y = False
                else:
                    print("Oops! Please enter a valid number: ")
            z = True
            while z:
                inp_position = int(input("Enter the position (positions are from 1 through 9): "))
                if (inp_position >= 1) and (inp_position <= 9) and (inp_position != 0) and (board[inp_position - 1] == "-"):
                    board[inp_position - 1] = inp
                    print_board(board)
                    z = False
                else:
                    print("This position is unavailable. please enter another position: ")


# there are 8 winning arrangements in this game (game 2), which are 3 horizontal, 3 vertical, and 2 diagonals
# checking for a winner in horizontal columns
def check_horizontal(player):
    i = 0
    while i < 7:
        if (board[i] == "-") or (board[i+1] == "-") or (board[i+2] == "-"):
            return
        else:
            if board[i] + board[i+1] + board[i+2] == 15:
                print("Congratulations!")
                print("Player " + str(player) + " won!")
                exit()
        i = i + 3


# checking for a winner in vertical rows
def check_vertical(player):
    i = 0
    while i < 3:
        if (board[i] == "-") or (board[i+3] == "-") or (board[i+6] == "-"):
            return
        else:
            if board[i] + board[i+3] + board[i+6] == 15:
                print("Congratulations!")
                print("Player " + str(player) + " won!")
                exit()
        i = i+1


# checking for a winner in the first diagonal
def check_diagonal1(player):
    if (board[0] == "-") or (board[4] == "-") or (board[8] == "-"):
        return
    else:
        if board[0] + board[4] + board[8] == 15:
            print("Congratulations!")
            print("Player " + str(player) + " won!")
            exit()


# checking for a winner in the second diagonal
def check_diagonal2(player):
    if (board[2] == "-") or (board[4] == "-") or (board[6] == "-"):
        return
    else:
        if board[2] + board[4] + board[6] == 15:
            print("Congratulations!")
            print("Player " + str(player) + " won!")
            exit()


# the game body
player = 1
while True:
    print_board(board)
    players(player)
    check_horizontal(player)
    check_vertical(player)
    check_diagonal1(player)
    check_diagonal2(player)
    check_tie(board)
    if player == 1:
        player = 2
    else:
        player = 1

