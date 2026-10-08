import socket
import threading


def handle_client(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)
    conn.close()


def start_server():
    server = socket.socket()
    server.bind(('localhost', 5000))
    server.listen(5)
    print("server running")

    while True:
        conn, addr = server.accept()
        print("Connected by", addr)
        threading.Thread(target=handle_client, args=(conn,), daemon=True).start()


if __name__ == "__main__":
    start_server()