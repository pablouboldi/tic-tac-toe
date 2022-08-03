import warnings
import numpy as np

warnings.simplefilter(action='ignore', category=FutureWarning)


def enter_data(matrix, user, number):
    if user == 1:
        matrix = np.where(matrix == number, 'X', matrix)
        if is_winner(matrix):
            user = 1
        else:
            user = 2

    elif user == 2:
        matrix = np.where(matrix == number, 'O', matrix)
        if is_winner(matrix):
            user = 2
        else:
            user = 1

    return matrix, user


def show_board(matrix):
    print('-----|-----|-----')
    for i in range(3):
        print(f'  {matrix[i][0]}  |  {matrix[i][1]}  |  {matrix[i][2]}  ')
        print('-----|-----|-----')
    return


def is_winner(matrix):
    for i in range(3):
        if matrix[0][i] == matrix[1][i] == matrix[2][i]:
            return True
        elif matrix[:, 0][i] == matrix[:, 1][i] == matrix[:, 2][i]:
            return True
    if matrix[0][0] == matrix[1][1] == matrix[2][2]:
        return True
    elif matrix[0][2] == matrix[1][1] == matrix[2][0]:
        return True
    else:
        return False


array = np.array(np.mat('1 2 3; 4 5 6; 7 8 9'), dtype=object)

count = 0
player = 1

show_board(array)

while count < 9 and is_winner(array) is not True:

    choice = int(input(f'\nPlayer {player}, enter the number you want:\n'))

    if choice not in range(1, 10) or choice not in array:
        print('\nThat is invalid. Try again.\n')
        show_board(array)
    else:
        count += 1
        array, player = enter_data(array, player, choice)
        show_board(array)

if count == 9:
    print("\nThat's a draw.")
else:
    print(f'\nPlayer {player} won! Congratulations!!')

print('Game Over!')
