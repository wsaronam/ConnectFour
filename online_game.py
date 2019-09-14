# Willy Saronamihardja 80408898 and Kenneth Chhan Yam 61791166.  ICS 32

import online_tools
import socket

def main():
    host = online_tools.ask_for_host()
    port = online_tools.ask_for_port()
    print ('Connecting...')
    try:
        program_connection = online_tools.connect(host, port)
    except:
        print('Sorry, cannot connect')
        #program_connection.close()
    else:
        print ('Connected.')
        connection_in = program_connection.makefile('r')
        connection_out = program_connection.makefile('w')
        username = online_tools.ask_for_username()
        message = 'I32CFSP_HELLO ' + username + '\r\n'
        connection_out.write(message)
        connection_out.flush()
        online_tools.read_line(program_connection)
        message = 'AI_GAME ' + '\r\n'
        connection_out.write(message)
        connection_out.flush()   
        online_tools.read_line(program_connection)    

    
        print(online_tools.play_game_for_red(online_tools.start, program_connection, connection_out))
    
    



if __name__ == '__main__':
    main()



