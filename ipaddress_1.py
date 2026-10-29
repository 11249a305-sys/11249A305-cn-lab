import socket
hostname = socket.gethostname()
ip_adress = socket.gethostbyname(hostname)
print("hostname:",hostname)
print("IP ADRESS:", ip_adress)