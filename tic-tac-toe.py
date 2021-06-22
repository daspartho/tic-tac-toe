def create_board():
    global board
    board = [x for x in range(9)]
    
def print_board():
    for i in range(0,7,3):
        for j in board[i:i+3]:
            print(j,end= '  ')
        print('\n')

def insert_letter(letter, pos):
    board[pos] = letter

def is_free(pos):
    return board[pos]==pos

def is_full():
    for i in board:
        if type(i) == int:
            return False
    return True

def move(letter):
    while True:
        pos = int(input(f'Enter a position to place an {letter} (0-8): '))
        assert pos in range(9)
        if is_free(pos):
            insert_letter(letter, pos)
            break
        else:
            print('Position already occupied!')
            
def winner():
    for i in range(3):
        if board[i]==board[i+3]==board[i+6]:
            return board[i]
    for i in range(0,7,3):
        if board[i]==board[i+1]==board[i+2]:
            return board[i]
    if board[0]==board[4]==board[8]:
        return board[0]
    if board[2]==board[4]==board[6]:
        return board[2]
    return None

def main():
    print('Welcome to Tic Tac Toe!')
    print('The board has positions 0-8 starting from the top left.')
    print()
    create_board()
    print_board()
    while not is_full() and not winner():
        move('X')
        print()
        print_board()
        if not is_full() and not winner():
            move('O')
            print()
            print_board()
    if winner():
        print(f'{winner()} wins!')
    elif is_full():
        print('Draw')
main()
