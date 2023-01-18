def show_board():
    for i in range(3):
        print(board[i])



def check_winner(arr, user_turn):
    for i in range(3):
        if arr[0][i] == arr[1][i] == arr[2][i] == user_turn:
            return True
    else:
        for i in range(3):
            if arr[i][0] == arr[i][1] == arr[i][2] == user_turn:
                return True
        else:        
            if arr[0][0] == arr[1][1] == arr[2][2] == user_turn:
                return True
            elif arr[2][0] == arr[1][1] == arr[0][2] == user_turn:
                return True

 
winner = ''
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
    if check_winner(board ,'X'):
        winner = 'X'
        is_game_on = False
    elif check_winner(board , 'O'):
        winner = 'O'
        is_game_on = False
    

print(f'the winner is {winner}')