def show_board():
    for i in range(3):
        print(board[i])


board = [['-','-','-'],['-','-','-'],['-','-','-',]]
show_board()
user_one = True
is_game_on = True
while is_game_on:
    user_input = input("where you want to put your mark(x,y)(splite your number with comma ,) ").split(',')
    if user_one:
        board[int(user_input[0])][int(user_input[1])] = 'O'
        user_one = False
    else:
        board[int(user_input[0])][int(user_input[1])] = 'X'
        user_one = True
    show_board()