
import socket, threading

pong = "+PONG\r\n"

def handle_client(client, addr):
    with client:
        while True:
            data = client.recv(1024)
            print("data received", data)
            if not data:
                break
            client.sendall(pong.encode())

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    while True:
        conn, recv = server_socket.accept() # wait for client
        threading.Thread(target=handle_client, args=(conn, recv)).start()