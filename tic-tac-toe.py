def create_board():
    # creates an array representing the board
    return [x for x in range(9)]
    
def print_board(board):
    # prints board
    for i in range(0,7,3): 
        for j in board[i:i+3]:
            print(j,end= '  ')
        print('\n') # change line after every 3rd character

def insert_letter(letter, pos, board):
    # Inserts letter at position
    board[pos] = letter

def is_free(pos, board):
    # Checks if the position if free
    return board[pos]==pos # returns True or False value

def is_full(board):
    # Checks if the board is full
    for i in board:
        if type(i) == int:
            return False
    return True

def move(letter, board):
    # Asks user to input a move and validate it, if valid adds it to board
    while True:
        pos = int(input(f'Enter a position to place an {letter} (0-8): '))
        try:
            assert pos in range(9) # Assert choice is valid
        except AssertionError:
            print('Invalid position! Try Again!')
            continue # try again
        if is_free(pos, board):
            insert_letter(letter, pos, board)
            break
        else:
            print('Position already occupied!')

def vertical_winner(board):
    """Check for winner vertically."""
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6]:
            return board[i]

def horizontal_winner(board):
    """Check for winner horizontally."""
    for i in range(0,7,3):
        if board[i]==board[i+1]==board[i+2]:
            return board[i]

def diagonal_winner(board):
    """Check for diagonal winner."""
    if board[0]==board[4]==board[8]:
        return board[0]
    if board[2]==board[4]==board[6]:
        return board[2]

def winner(board): # returns winning letter if there is a winner else returns None
    if _ := vertical_winner(board):
        return _
    if _ := horizontal_winner(board):
        return _
    if _ := diagonal_winner(board):
        return _
    return None

def do_move(c):
    """Accept a move and render on the board."""
    move(c)
    print()
    print_board()

def main():
    # Main game loop
    print('Welcome to Tic Tac Toe!')
    print('The board has positions 0-8 starting from the top left.')
    print()
    board = create_board()
    print_board(board)
    while not is_full(board) and not winner(board): # run until someone wins or the board is full
        move('X', board)
        print()
        print_board(board)
        if is_full(board) or winner(board):
            # breaks out of the loop if 'X' alredy won by the last move or the board got full
            break
        move('O', board)
        print()
        print_board(board)
    if winner(board):
        print(f'{winner(board)} wins!')
    elif is_full(board):
        print('Tie! No more spaces left.')
        
while True:
    main()
    print()
    choice=input('Do you want to play again? (Y/N): ').upper()
    print()
    if choice=='N':
        print('OK')
        break # terminates
