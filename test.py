def check_winner(arr):
    for i in range(3):
        for j in range(3):
            print(f'if arr{i}{j} == arr{i}{j}:')
board = [['0','1','2'],['3','4','5'],['6','7','8']]
print(check_winner(board))