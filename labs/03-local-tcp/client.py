import socket

with socket.create_connection(("127.0.0.1", 50505), timeout=5) as client:
    client.sendall(b"Hello from the client")
    print(client.recv(1024).decode("utf-8"))
