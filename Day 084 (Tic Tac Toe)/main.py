print("Welcome to TIC TAC TOE!!")
pos = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

game_on = True


def display_board():
    board = (f'{pos[0]} | {pos[1]} | {pos[2]} \n'
             f'---------\n'
             f'{pos[3]} | {pos[4]} | {pos[5]} \n'
             f'---------\n'
             f'{pos[6]} | {pos[7]} | {pos[8]} \n')
    print(board)


start_game = input("Type 'yes' to play else type 'no': ").lower()
if start_game == 'yes':
    print('\n')
    display_board()

    while game_on:
        player_move1 = input("Type the number you'd like to replace: ")
        player_char = input("Type 'X' or 'O': ").upper()

        for x in pos:
            if player_move1 == x:
                pos[int(player_move1) - 1] = player_char

        display_board()

        if (pos[0] == pos[1] == pos[2]) or (pos[0] == pos[3] == pos[6]) or (pos[3] == pos[4] == pos[5]) or (
                pos[6] == pos[7] == pos[8]) or (pos[1] == pos[4] == pos[7]) or (pos[2] == pos[5] == pos[8]) or (
                pos[0] == pos[4] == pos[8]) or (pos[2] == pos[4] == pos[6]):
            game_on = False
            player1 = 0
            player2 = 0
            for move in pos:
                if move == 'X':
                    player1 += 1
                if move == 'O':
                    player2 += 2
            if player1 > player2:
                print("'X' is the Winner!!")
            else:
                print("'O' is the Winner!!")
