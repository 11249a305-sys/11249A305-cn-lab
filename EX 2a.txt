import socket

# Create a TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set a timeout (e.g., 5 seconds) so the client doesn't hang forever if the server is offline
client.settimeout(5.0)

try:
    # Connect to the HTTP server
    client.connect(('localhost', 8080))

    # Create a basic HTTP GET request
    http_request = (
        "GET / HTTP/1.1\r\n"
        "Host: localhost\r\n"
        "Connection: close\r\n"
        "\r\n"
    )

    # Send the request to the HTTP server
    client.sendall(http_request.encode())

    # Gather all data sent back by the server
    response = b""
    while True:
        try:
            chunk = client.recv(1024)
            if not chunk:
                break
            response += chunk
        except socket.timeout:
            print("Warning: Server response timed out.")
            break

    print("--- Received HTTP Response ---")
    print(response.decode(errors="replace"))   # <-- Only this line is changed

except ConnectionRefusedError:
    print("Error: Could not connect to the server. Make sure your server.py is running on port 8080!")
finally:
    client.close()