def show_board():
    for i in range(3):
        print(board[i])


board = [['-','-','-'],['-','-','-'],['-','-','-',]]
show_board()

wh
    user_input = input("where you want to put your mark(x,y)(splite your number with comma ,) ").split(',')

    board[int(user_input[0])][int(user_input[1])] = 'O'
    show_board()