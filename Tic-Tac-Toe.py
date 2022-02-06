# 12/13/2021 - 1/2/2022
'''
This is 2 player Tic-Tac_Toe. The input corresponds to the modern numpad:
_|_|_    7|8|9
_|_|_ -> 4|5|6
 | |     1|2|3
'''

def pick_player():
    global player_choice #The avatar the player wants to be
    player = input("Player 1: Do you want to be X or O?: ")
    global x_player
    global o_player
    while 1==1:
        if player == "O" or player == "0" or player == "o":
            player_choice = "O"
            o_player = "Player 1"
            x_player = "Player 2"
            print("Player 1 is O and Player 2 is X.\nPlayer 1 goes first.")
            break
        elif player == "X" or player == "x":
            player_choice = "X"
            x_player = "Player 1"
            o_player = "Player 2"
            print("Player 1 is X and Player 2 is O.\nPlayer 1 goes first.")
            break
        else:
            player = input("Player 1: Please enter either X or O: ")
    global which_player #Which Player is currently playing
    which_player = 1 
    global player_name #The name of the player
    player_name = "Player 1"
    return player_choice

row1 = ["_","|","_","|","_"]
row2 = ["_","|","_","|","_"]
row3 = [" ","|"," ","|"," "]

xU = "X̲"
oU = "O̲"    

def valid_user_input(player_name):
    global choice
    choice = input("{}: Please Enter a number from 1-9: ".format(player_name))
    while 1 == 1:
        if choice.isdigit() == True:
            if int(choice) >= 1 and int(choice) <= 9:
                if int(choice) == 7:
                    if row1[0] == xU or row1[0] == oU:
                        choice = input("Please enter a number that is already not taken: ")
                    else:
                        break
                elif int(choice) == 8:
                    if row1[2] == xU or row1[2] == oU:
                        choice = input("Please enter a number that is already not taken: ")
                    else:
                        break
                elif int(choice) == 9:
                    if row1[4] == xU or row1[4] == oU:
                        choice = input("Please enter a number that is already not taken: ")
                    else:
                        break
                elif int(choice) == 4:
                    if row2[0] == xU or row2[0] == oU:
                        choice = input("Please enter a number that is already not taken: ")
                    else:
                        break
                elif int(choice) == 5:
                    if row2[2] == xU or row2[2] == oU:
                        choice = input("Please enter a number that is already not taken: ")
                    else:
                        break
                elif int(choice) == 6:
                    if row2[4] == xU or row2[4] == oU:
                        choice = input("Please enter a number that is already not taken: ")
                    else:
                        break
                elif int(choice) == 1:
                    if row3[0] == "X" or row3[0] == "O":
                        choice = input("Please enter a number that is already not taken: ")
                    else:
                        break
                elif int(choice) == 2:
                    if row3[2] == "X" or row3[2] == "O":
                        choice = input("Please enter a number that is already not taken: ")
                    else:
                        break
                elif int(choice) == 3:
                    if row3[4] == "X" or row3[4] == "O":
                        choice = input("Please enter a number that is already not taken: ")
                    else:
                        break
            else:
                choice = input("You have entered {}. The number should be greater than 0 and less than 10. Please Try Again: ".format(int(choice)))
        elif choice.isdigit() == False:
            choice = input("Please make sure to enter a valid number from 1-9: ")
    return int(choice)

def tic_tac_toe_input(player_choice, choice):
    if choice == 7:
        if player_choice == "X":
            row1[0] = xU
        elif player_choice == "O":
            row1[0] = oU
    elif choice == 8:
        if player_choice == "X":
            row1[2] = xU
        elif player_choice == "O":
            row1[2] = oU
    elif choice == 9:
        if player_choice == "X":
            row1[4] = xU
        elif player_choice == "O":
            row1[4] = oU
    ################################
    elif choice == 4:
        if player_choice == "X":
            row2[0] = xU
        elif player_choice == "O":
            row2[0] = oU
    if choice == 5:
        if player_choice == "X":
            row2[2] = xU
        elif player_choice == "O":
            row2[2] = oU
    if choice == 6:
        if player_choice == "X":
            row2[4] = xU
        elif player_choice == "O":
            row2[4] = oU
    ###############################
    if choice == 1:
        if player_choice == "X":
            row3[0] = "X"
        elif player_choice == "O":
            row3[0] = "O"
    if choice == 2:
        if player_choice == "X":
            row3[2] = "X"
        elif player_choice == "O":
            row3[2] = "O"
    if choice == 3:
        if player_choice == "X":
            row3[4] = "X"
        elif player_choice == "O":
            row3[4] = "O"
    #############################
    
    return row1, row2, row3

x = 1

def check_for_winner(row1, row2, row3):
    global restart
    while 1 == 1: 
        if row1[0] == xU and row1[2] == xU and row1[4] == xU:
            restart = input("{} has won! Do you want to play again (Y/N): ".format(x_player))
        elif row1[0] == oU and row1[2] == oU and row1[4] == oU:
            restart = input("{} has won! Do you want to play again (Y/N): ".format(o_player))
        elif row2[0] == oU and row2[2] == oU and row2[4] == oU:
            restart = input("{} has won! Do you want to play again (Y/N): ".format(o_player))
        elif row2[0] == xU and row2[2] == xU and row2[4] == xU:
            restart = input("{} has won! Do you want to play again (Y/N): ".format(x_player))
        elif row3[0] == "X" and row3[2] == "X" and row3[4] == "X":
            restart = input("{} has won! Do you want to play again (Y/N): ".format(x_player))
        elif row3[0] == "O" and row3[2] == "O" and row3[4] == "O":
            restart = input("{} has won! Do you want to play again (Y/N): ".format(o_player))
        elif row1[0] == xU and row2[2] == xU and row3[4] == "X":
            restart = input("{} has won! Do you want to play again (Y/N): ".format(x_player))
        elif row1[0] == oU and row2[2] == oU and row3[4] == "O":
            restart = input("{} has won! Do you want to play again (Y/N): ".format(o_player))
        elif row1[4] == xU and row2[2] == xU and row3[0] == "X":
            restart = input("{} has won! Do you want to play again (Y/N): ".format(x_player))
        elif row1[4] == oU and row2[2] == oU and row3[0] == "O":
            restart = input("{} has won! Do you want to play again (Y/N): ".format(o_player))
        elif row1[0] == xU and row2[0] == xU and row3[0] == "X":
            restart = input("{} has won! Do you want to play again (Y/N): ".format(x_player))
        elif row1[0] == oU and row2[0] == oU and row3[0] == "O":
            restart = input("{} has won! Do you want to play again (Y/N): ".format(o_player))
        elif row1[2] == xU and row2[2] == xU and row3[2] == "X":
            restart = input("{} has won! Do you want to play again (Y/N): ".format(x_player))
        elif row1[2] == oU and row2[2] == oU and row3[2] == "O":
            restart = input("{} has won! Do you want to play again (Y/N): ".format(o_player))
        elif row1[4] == xU and row2[4] == xU and row3[4] == "X":
            restart = input("{} has won! Do you want to play again (Y/N): ".format(x_player))
        elif row1[4] == oU and row2[4] == oU and row3[4] == "O":
            restart = input("{} has won! Do you want to play again (Y/N): ".format(o_player))
        elif (row1[0] == xU or row1[0] == oU) and (row1[2] == xU or row1[2] == oU) and (row1[4] == xU or row1[4] == oU) and (row2[0] == xU or row2[0] == oU) and (row2[2] == xU or row2[2] == oU) and (row2[4] == xU or row2[4] == oU) and (row3[0] == "X" or row3[0] == "O") and (row3[2] == "X" or row3[2] == "O") and (row3[4] == "X" or row3[4] == "O"):
            restart = input("The Game was a Draw! Do you want to play again (Y/N): ")
        else:
            restart = "continue"
            break
        
        while 1 == 1:
            if restart != "Y" and restart != "N" and restart != "continue":
                restart = input("Please enter either Y or N: ")
            else:
                break
        
        return restart
    

def display(r1, r2, r3):
    print(''.join(r1[0:]))
    print(''.join(r2[0:]))
    print(''.join(r3[0:]))

print("Welcome to Tic-Tac-Toe!")
pick_player()

while x == 1:
    valid_user_input(player_name)
    tic_tac_toe_input(player_choice, int(choice))
    display(row1,row2,row3)
    check_for_winner(row1, row2, row3)

    if restart == "Y":
        x = 1
        pick_player()
        row1 = ["_","|","_","|","_"]
        row2 = ["_","|","_","|","_"]
        row3 = [" ","|"," ","|"," "]
        which_player = 2
        player_name = "Player 1"
        if player_choice == "X":
            player_choice = "O"
        elif player_choice == "O":
            player_choice = "X"
    elif restart == "N":
        print("Thank you for playing Tic-Tac-Toe! \nMade by Bhuvan. Coded entirely in Python.")
        x = 2
        break
    elif restart == "continue":
        pass

    if which_player == 1:
        which_player = 2
        player_name = "Player 2"
    elif which_player == 2:
        which_player = 1
        player_name = "Player 1"
    
    if player_choice == "X":
        player_choice = "O"
    elif player_choice == "O":
        player_choice = "X"