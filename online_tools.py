# Willy Saronamihardja 80408898 and Kenneth Chhan Yam 61791166.  ICS 32

import socket
import connectfour


_SHOW_DEBUG_TRACE = True



def ask_for_port () -> int:
    while True:
        try:
            port = int(input('Port: '))
            if port < 0 or port > 65535:
                print ('Ports must be integers between 0 and 65535')
            else:
                return port
        except ValueError:
            print ('Ports must be integers between - and 65535')
            

def ask_for_host() -> str:
    while True:
        host = input('Host: ').strip()
        
        if host == '':
            print('Please specify a host(name or ip address)')
        else:
            return host


def ask_for_username() -> str:
    name = input('Please enter a username with no spaces: ').strip()
    newname = name.replace(' ', '')
    if len(newname) == 0:
        ask_for_username()
    else:
        return newname
        


def connect(host: str, port: int) -> 'connection':
    the_socket = socket.socket()
    the_socket.connect((host, port))
    connection = the_socket
    return connection



start = connectfour.new_game()


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
        print()
        


def drop_or_pop() -> str:
    answer = ''
##    answer = input()
##    ans_list = answer.split(' ')
    while answer != 'D' and answer != 'P':
        answer = input('Would you like to drop or pop? Type D or P:  ')
        answer = answer.upper()
    return answer




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



def play_game_for_red(position: 'GameState', connection: 'connection', connectionout: 'Connection Out') -> 'GameState' or None:    
    
    connectfour.winner(position)
    if connectfour.winner(position) == connectfour.NONE:
        move = drop_or_pop()
        if move == 'D':
            column_num = overlimit(position)
            
            nextmove = connectfour.drop(position, column_num)
            board(nextmove)
            message = 'DROP ' + str(column_num) + '\r\n'
            connectionout.write(message)
            connectionout.flush()
            read_line(connection)
            server_turn = read_line(connection)
            read_line(connection)
            server_move = server_response_dorp (server_turn)
            server_placing = server_response_num (server_turn)
            print (server_move)
            return play_game_for_yellow(nextmove, server_move, server_placing)
        elif move == 'P':
            column_num = int(input('Enter a column number from 1-7: ')) - 1
            try:
                nextmove = connectfour.pop(position, column_num)
            except:
                play_game(position)
            else:
                board(nextmove)
                return play_game_for_yellow(nextmove, server_move, server_placing)
    else:
        thewinner = connectfour.winner(position)
        if thewinner == 1:
            print ('Red wins!')
        elif thewinner == 2:
            print ('Yellow wins!')


def play_game_for_yellow(position: 'GameState', dorp: str, col: str) -> 'GameState' or None:    
    
    connectfour.winner(position)
    print (dorp + col)
    if connectfour.winner(position) == connectfour.NONE:
        if dorp == 'D':
            nextmove = connectfour.drop(position, col)
            board(nextmove)
            return play_game_for_red(nextmove, connection, connectionout)
        elif dorp == 'P':
            column_num = int(input('Enter a column number from 1-7: ')) - 1
            try:
                nextmove = connectfour.pop(position, column_num)
            except:
                play_game(position)
            else:
                board(nextmove)
                return play_game_for_red(nextmove, connection, connectionout)
    else:
        thewinner = connectfour.winner(position)
        if thewinner == 1:
            print ('Red wins!')
        elif thewinner == 2:
            print ('Yellow wins!')



#return play_game_for_red(nextmove, connection, connectionout)


def read_line(connection: 'Connection') -> str:
    response_bytes = connection.recv(4096)
    response_text = response_bytes.decode(encoding = 'utf-8')
    print (response_text)
    return response_text


def server_response_dorp (answer: str) -> str:
    d_or_p = answer[0]
    return d_or_p


def server_response_num (answer: str) -> int:
    num = answer[-1]
    return int(num)

