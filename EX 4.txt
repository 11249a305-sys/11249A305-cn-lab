import socket
import threading

clients = []

def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")

    while True:
        try:
            message = client_socket.recv(1024).decode()

            if not message:
                break

            print(f"Received from {client_address}: {message}")

            # Broadcast to all other clients
            for client in clients:
                if client != client_socket:
                    client.sendall(message.encode())

        except Exception as e:
            print(f"Error with {client_address}: {e}")
            break

    # Remove disconnected client
    if client_socket in clients:
        clients.remove(client_socket)

    client_socket.close()
    print(f"{client_address} disconnected")


def chat_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Allow immediate reuse of the port
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind(('localhost', 55555))
    server_socket.listen(5)

    print("Server listening on port 55555...")

    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)

        thread = threading.Thread(
            target=handle_client,
            args=(client_socket, client_address)
        )
        thread.daemon = True
        thread.start()


if __name__ == '__main__':
    chat_server()