import socket, asyncio

pong = "+PONG\r\n"

async def handle_client(client):
    loop = asyncio.get_event_loop()
    while req := await loop.sock_recv(client, 1024):
        print("received request", req, client)
        await loop.sock_sendall(client, pong.encode())

async def async_main():
    server = socket.create_server(('localhost', 6379), reuse_port=True)
    server.setblocking(False)
    server.listen()
    loop = asyncio.get_event_loop()
    while True:
        client, _ = await loop.sock_accept(server)
        loop.create_task(handle_client(client))