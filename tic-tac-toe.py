def create_board():
    global board
    board = [x for x in range(9)]
    
def print_board():
    for i in board:
        if i%3==0:
            print('\n')
        print(i,end='  ')
