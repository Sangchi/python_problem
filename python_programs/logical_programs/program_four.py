'''
4. Cross Game or Tic-Tac-Toe Game
a. Desc -> Write a Program to play a Cross Game or Tic-Tac-Toe Game. Player 1
is the Computer and the Player 2 is the user. Player 1 take Random Cell that is
the Column and Row.
b. I/P -> Take User Input for the Cell i.e. Col and Row to Mark the ‘X’
c. Logic -> The User or the Computer can only take the unoccupied cell. The Game
is played till either wins or till draw...
d. O/P -> Print the Col and the Cell after every step.
e. Hint -> The Hints is provided in the Logic. Use Functions for the Logic
'''

def print_board(board):
    for row in board:
        print("-----------")
        print(" | ".join(row))
        print("-----------")

def check_winner(board, player):
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    if(board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player):
        return True
    
    return False

def check_draw(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def play_game():
    board = [[' ']*3 for _ in range(3)]
    players = ['X', 'O']
    turn = 0
    
    while True:
        current_player = players[turn % 2]
        print_board(board)
        
        
        valid_move = False
        while not valid_move:
            try:
                row = int(input(f"Player {current_player}, enter row (0-2): "))
                col = int(input(f"Player {current_player}, enter column (0-2): "))
                if 0 <= row <= 2 and 0 <= col <= 2:
                    if board[row][col] == ' ':
                        valid_move = True
                    else:
                        print("That position is already taken. Try again.")
                else:
                    print("Please enter a valid row and column (0-2).")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
      
        board[row][col] = current_player
        

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        turn += 1

play_game()



'''
output-

-----------
X | X | O
-----------
-----------
O | O | X
-----------
-----------
X | X | O
-----------
It's a draw!
'''