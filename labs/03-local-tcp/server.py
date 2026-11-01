import socket

HOST = "127.0.0.1"
PORT = 50505

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"Listening on {HOST}:{PORT}")
    conn, address = server.accept()
    with conn:
        print("Connected:", address)
        data = conn.recv(1024)
        print("Received:", data.decode("utf-8", errors="replace"))
        conn.sendall(b"Hello from the local TCP server")
