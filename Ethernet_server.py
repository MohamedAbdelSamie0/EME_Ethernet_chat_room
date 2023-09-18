import socket
import threading

# HOST = '192.168.33.117'
HOST = 'localhost'
PORT = 12345

class ChatServer:
    def __init__(self):
        self.clients = []

    def listen(self, host, port):
        print('Server Running')
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(15)

        while True:
            client_socket, client_address = self.server_socket.accept()
            self.clients.append(client_socket)

            # Create a new thread to handle the client
            client_thread = threading.Thread(target=self.client_handler, args=(client_socket,))
            client_thread.start()

    def client_handler(self, client_socket):
        while True:
            # Receive data from the client
            message = client_socket.recv(1024)

            # If the client has disconnected, remove it from the list of clients
            if not message:
                self.clients.remove(client_socket)
                break

            # Send the message to all other clients
            for other_client in self.clients:
                if other_client != client_socket:
                    other_client.send(message)

    def stop(self):
        for c in self.clients:
            c.close()
        self.server_socket.close()

if __name__ == '__main__':
    # create new chat server object
    server = ChatServer()
    # start server
    server.listen(host= HOST, port= PORT)

    # keep server running untill user closes
    print("----------------------------------")
    input("Press any key to close server....")

    # stop server
    ChatServer.stop()