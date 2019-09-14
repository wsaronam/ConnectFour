# Willy Saronamihardja 80408898 and Kenneth Chhan Yam 61791166.  ICS 32

import connectfour



def obtainanswer() -> str:
    answer = ''
    while answer != 'D' and answer != 'P':
        answer = input('Would you like to drop or pop? Type D or P:  ')
        answer = answer.upper()
    return answer


def board(game_state: 'GameState') -> None:
    
    print ('1 2 3 4 5 6 7')
    for i in range(connectfour.BOARD_ROWS):
        row_board = ''
        for j in range(connectfour.BOARD_COLUMNS):
            if game_state.board[j][i] == 0:
                row_board += ". "
            elif game_state.board[j][i] == 1:
                row_board += "R "
            elif game_state.board[j][i] == 2:
                row_board += "Y "
        print(row_board)
        print ()

            
def overlimit(game_state: 'GameState') -> int:
    check_col = 0
    while check_col > 7 or check_col < 1:
        check_col = int(input('Enter a column number from 1-7: ')) - 1
        if check_col > 6 or check_col < 0:
            print ('Not in range.')
        elif game_state.board[check_col][0] != 0:
            print ('Invalid move.')
        else:
            return check_col


def underlimit (game_state: 'GameState') -> int:
    check_col = 0
    while check_col > 7 or check_col < 1:
        check_col = int(input('Enter a column number from 1-7: ')) - 1
        if check_col > 6 or check_col < 0:
            print ('Not in range.')
        elif game_state.board[check_col][-1] == connectfour.NONE:
            print ('Invalid move.')
        elif game_state.turn == connectfour.RED:
            if game_state.board[check_col][-1] == connectfour.YELLOW:
                print ('Can not pop')
        elif game_state.turn == connectfour.YELLOW:
            if game_state.board[check_col][-1] == connectfour.RED:
                print ('Can not pop')
        else:
            return check_col
