import socket
import threading

HOST = 'localhost'
PORT = 12345

client_name = input('Enter your name: ')

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def receive():
    while True:
        try:
            # receive message from server
            data = client_socket.recv(1024)
            # print received message
            print(data.decode())

        except Exception as e:
            print(e)
            client_socket.close()
            break

def send():
    while True:
        # send a message to server
        message = f'{client_name}' + '->' + input()
        client_socket.send(message.encode())


if __name__ == '__main__':
    receiveThread = threading.Thread(target=receive).start()
    send_thread = threading.Thread(target=send).start()