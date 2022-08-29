# ********************************************************************************************
    # Lab: Network Programming: Sockets.
    # Course: ST0255 - Telemática.
    # TCP-Socket Server.
# ********************************************************************************************

#Import libraries for networking communication...

import socket
import constants

#Create a socket...
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Main function...
def main():
    print('***********************************')
    print('Server is running...')
    print('IP Addr:',constants.SERVER_ADDRESS )
    print('Port:', constants.PORT)
    create_server_socket()
    
# Function to start server process...
def create_server_socket():
    tuple_connection = (constants.SERVER_ADDRESS,constants.PORT)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(tuple_connection)
    server_socket.listen(constants.BACKLOG)
    print('Socket is listening...', server_socket.getsockname())        
        
    # Loop for waiting new connections...
    while True:
        client_connection, client_address = server_socket.accept()
        print(f'New incoming conection is accepted. Remote IP adress: {client_address[0]}.Port: {client_address[1]}')
        while True:
            data_recevived = client_connection.recv(constants.RECV_BUFFER_SIZE)
            remote_string = str(data_recevived.decode(constants.ENCONDING_FORMAT))
            remote_command = remote_string.split()
            command = remote_command[0]
            print (f'Data received from: {client_address[0]}:{client_address[1]}')
            print(command)
            if (command == constants.HELO):
                response = '100 OK\n'
                client_connection.sendall(response.encode(constants.ENCONDING_FORMAT))
            elif (command == constants.QUIT):
                response = '200 BYE\n'
                client_connection.sendall(response.encode(constants.ENCONDING_FORMAT))
                print(f'Now, client {client_address[0]}:{client_address[1]} is disconnected...')
                break                                      
            elif (command == constants.DATA):
                response = "300 DRCV\n"
                client_connection.sendall(response.encode(constants.ENCONDING_FORMAT))
            else:
                response = '400 BCMD\n\rCommand-Description: Bad command\n\r'
                client_connection.sendall(response.encode(constants.ENCONDING_FORMAT))
        client_connection.close()


if __name__ == '__main__':
    main()