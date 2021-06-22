def create_board():
    # creates an array representing the board
    global board
    board = [x for x in range(9)]
    
def print_board():
    # prints board
    for i in range(0,7,3): 
        for j in board[i:i+3]:
            print(j,end= '  ')
        print('\n') # change line after every 3rd character

def insert_letter(letter, pos):
    # Inserts letter at position
    board[pos] = letter

def is_free(pos):
    # Checks if the position if free
    return board[pos]==pos # returns True or False value

def is_full():
    # Checks if the board is full
    for i in board:
        if type(i) == int:
            return False
    return True

def move(letter):
    # Asks user to input a move and validate it, if valid adds it to board
    while True:
        pos = int(input(f'Enter a position to place an {letter} (0-8): '))
        try:
            assert pos in range(9) # Assert choice is valid
        except AssertionError:
            print('Invalid position! Try Again!')
            continue # try again
        if is_free(pos):
            insert_letter(letter, pos)
            break
        else:
            print('Position already occupied!')
            
def winner(): # returns winning letter if there is a winner else returns None
    # Checks rows for a straight line
    for i in range(3):
        if board[i]==board[i+3]==board[i+6]:
            return board[i]
    # Checks columns for a straight line
    for i in range(0,7,3):
        if board[i]==board[i+1]==board[i+2]:
            return board[i]
    # Checks diagonals for a straight line
    if board[0]==board[4]==board[8]:
        return board[0]
    if board[2]==board[4]==board[6]:
        return board[2]
    return None

def main():
    # Main game loop
    print('Welcome to Tic Tac Toe!')
    print('The board has positions 0-8 starting from the top left.')
    print()
    create_board()
    print_board()
    while not is_full() and not winner(): # run until someone wins or the board is full
        move('X')
        print()
        print_board()
        if is_full() or winner():
            # breaks out of the loop if 'X' alredy won by the last move or the board got full
            break
        move('O')
        print()
        print_board()
    if winner():
        print(f'{winner()} wins!')
    elif is_full():
        print('Tie! No more spaces left.')
        
while True:
    main()
    print()
    choice=input('Do you want to play again? (Y/N): ').upper()
    print()
    if choice=='Y':
         continue # next iteration
    print('OK')
    break # terminates
