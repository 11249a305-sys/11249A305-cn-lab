import socket


def echo_server():
    server_socket = None

    try:
        # Create TCP socket (IPv4 + TCP)
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Allow address reuse
        server_socket.setsockopt(
            socket.SOL_SOCKET,
            socket.SO_REUSEADDR,
            1
        )

        # Bind to localhost and port
        server_socket.bind(("127.0.0.1", 65432))

        # Listen for incoming connections
        server_socket.listen(5)

        print("Server listening on port 65432...")

        while True:
            # Accept client connection
            connection, client_address = server_socket.accept()

            print(f"Connected by {client_address}")

            try:
                while True:
                    # Receive data
                    data = connection.recv(1024)

                    # Client disconnected
                    if not data:
                        break

                    message = data.decode()
                    print(f"Received: {message}")

                    # Echo the same data back
                    connection.sendall(data)

            finally:
                connection.close()
                print("Client disconnected\n")

    except KeyboardInterrupt:
        print("\nServer stopped manually.")

    except Exception as e:
        print("Error:", e)

    finally:
        if server_socket is not None:
            server_socket.close()


if __name__ == "__main__":
    echo_server()