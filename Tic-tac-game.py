from IPython.display import clear_output
#Display TicTac board

def display_board(board):
    print('-------------------')
    print('      |     |    ')
    print('  '+board[1]+'   |  '+board[2]+'  |  '+board[3]+'  ')
    print('      |     |    ')
    print('-------------------')
    print('      |     |    ')
    print('  '+board[4]+'   |  '+board[5]+'  |  '+board[6]+'  ')
    print('      |     |    ')
    print('-------------------')
    print('      |     |    ')
    print('  '+board[7]+'   |  '+board[8]+'  |  '+board[9]+'  ')
    print('      |     |    ')
    print('-------------------')
#Get player names
def player_name():
    print('PLAYERS, ENTER YOUR NAMES')
    print('WHO PLAYS FIRST WILL BE SELECTED AT RANDOM')
    player1 = input('PLAYER1 ENTER YOUR NAME: ')
    player2 = input('PLAYER2 ENTER YOUR NAME: ')
    return player1, player2
    #Get player Character
def player_input(player1, player2):
    
    player_choice_input = 'invalid'
    while True:
        player_choice_input = input(f'{player1}, choose your input (X or O): ')
        if player_choice_input not in ['X', 'x', 'O', 'o']:
            print('Sorry, I don’t understand what you are saying. Please type a correct value.')
            continue
        else:
            if player_choice_input == 'X' or player_choice_input == 'x':
                player1_marker = 'X'
                player2_marker = 'O'
                print(f'{player1} will use X.')
                print(f'{player2} will use O.')
            else:
                player1_marker = 'O'
                player2_marker = 'X'
                print(f'{player1} will use O.')
                print(f'{player2} will use X.')
            
            return player1_marker, player2_marker
 #Check win
def win_check(board, mark):
    if board[1] == board[2] == board[3] == mark or board[1] == board[4] == board[7] == mark or board[2] == board[5] == board[8] == mark or board[3] == board[6] == board[9] == mark or board[4] == board[5] == board[6] == mark or board[7] == board[8] == board[9] == mark or board[1] == board[5] == board[9] == mark or board[3] == board[5] == board[7] == mark:
        return True
    else:
        return False
import random
#Check which player will go first
def choose_first(player1, player2, player1_marker, player2_marker):
    if random.randint(1,2) == 1:
        clear_output()
        print(f'{player1} goes first')
        print('\n')
        print(f'{player1} is playing with {player1_marker}')
        print(f'{player2} is playing with {player2_marker}')
        return player1
    else:
        clear_output()
        print(f'{player2} goes first')
        print('\n')
        print(f'{player1} is playing with {player1_marker}')
        print(f'{player2} is playing with {player2_marker}')
        return player2
#Check if there is space in that position
def space_check(board, position):
    return board[position] == ' '
#Check if board is full
def full_board_check(board):
    if ' ' not in board[1:9]:
        return True
    else:
        return False
#Place marker in the position which the player selected on the board 
def player_choice(board, marker, player):
    choice = 0
    acceptable_range = range(0, 10)
    while True:
        choice = input(f'{player} pick a position: ')
        if choice.isdigit() == True:
            position = int(choice)
            if position in acceptable_range:
                if position == 0:
                    print('Zero is not part of the position to be picked')
                elif space_check(board, position):
                    clear_output()
                    print(f'{player} picked position {position}')
                    board[position] = marker
                    return board
                else:
                    print('That position is already occupied. Please choose another position.')
            elif position not in acceptable_range:
                print("Invalid position. Please choose a number between 1 and 9.")
        else:
            print("Invalid input. Please enter a number between 1 and 9.")
#Check to continue game or not
def replay():
    choice = 'wrong'
    
    while choice not in ['Y', 'y', 'N', 'n']:
        choice = input('Keep playing? (Y or N): ')
        if choice not in ['Y', 'y', 'N', 'n']:
            print('Sorry, I dont understand, please choose Y or N')
            continue
        if choice.lower() == 'y':
            return True
        else:
            clear_output()
            return False
print('WELCOME TO TIC TAC TOE GAME CREATED BY TOKS')
print('THE POSITIONS ARE MARKED FROM (1-9) IN THE ORDER BELOW:') 
print(f" {1} | {2} | {3} ")
print("---|---|---")
print(f" {4} | {5} | {6} ")
print("---|---|---")
print(f" {7} | {8} | {9} ")
print('\n')
player1, player2 = player_name()

player1_marker, player2_marker = player_input(player1, player2)
    
turn = choose_first(player1, player2, player1_marker, player2_marker)

while True:
    game_on = True
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']    
    
    display_board(board)
    
    print('\n')

    while game_on:
        
        if turn == player1:
            new_board = player_choice(board, player1_marker, player1)
            print(f'{player1} is playing with {player1_marker}')
            print(f'{player2} is playing with {player2_marker}')
            display_board(new_board)
            if win_check(board, player1_marker) == True:
                print(f'{player1} has won the game, congratulations')
                game_on = False
            elif full_board_check(board) == True:
                print('GAME ENDED IN A DRAW')
                game_on = False
            else:
                turn = player2
                
        elif turn == player2:
            new_board = player_choice(board, player2_marker, player2)
            print(f'{player1} is playing with {player1_marker}')
            print(f'{player2} is playing with {player2_marker}')
            display_board(new_board)
            if win_check(board, player2_marker) == True:
                print(f'{player2} has won the game, congratulations')
                game_on = False
            elif full_board_check(board) == True:
                print('GAME ENDED IN A DRAW')
                game_on = False
            else:
                turn = player1
    if replay() == True:
        turn = choose_first(player1, player2, player1_marker, player2_marker)
    else:
        display_board(board)
        print('THANK YOU FOR PLAYING')
        break
print('Bye bye')