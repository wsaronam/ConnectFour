# Willy Saronamihardja 80408898 and Kenneth Chhan Yam 61791166.  ICS 32

import local_tools
import connectfour



start = connectfour.new_game()
                
    
def run_game(position: 'GameState') -> 'GameState' or None:    
    
    connectfour.winner(position)
    
    if connectfour.winner(position) == connectfour.NONE:
        theanswer = local_tools.obtainanswer()
        if theanswer == 'D':
            column_num = local_tools.overlimit(position)
            
            nextstep = connectfour.drop(position, column_num)
            local_tools.board(nextstep)
            return run_game(nextstep)
        elif theanswer == 'P':
            column_num = int(input('Enter a column number from 1-7: ')) - 1
            try:
                nextstep = connectfour.pop(position, column_num)
            except:
                run_game(position)
            else:
                local_tools.board(nextstep)
                return run_game(nextstep)
    else:
        thewinner = connectfour.winner(position)
        if thewinner == 1:
            print ('Red wins!')
        elif thewinner == 2:
            print ('Yellow wins!')
        




if __name__ == '__main__':  
    run_game(start)


