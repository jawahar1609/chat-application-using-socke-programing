"""
This is an implementation of server with sockets for chat room
We use concepts of multi-threading to handle multiple clients.

We will be denoting server-side related messages with [*]
[+] -> New client connected
[-] -> Client disconnected

> Author: Team-3
"""

# import necessary libraries
import socket
from threading import Thread
from colorama import Fore, Back, Style, init

# Initialize to print out colors in cmd prompt
init(convert=True)

# We are using TCP protocol
ssock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Make the port reuseable
ssock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# server's host address
host = socket.gethostname()
port = 5000

# bind the socket to the address
ssock.bind((host, port))

# Keeps a backlog of 5 connections
ssock.listen(5)

print(f"\n{Back.BLUE}============================== Server Room =============================={Style.RESET_ALL}\n")
print(f"[*]{Fore.GREEN} Listening to incoming connections at {host}:{port}{Fore.RESET}")

# Add connected clients to the setcm
clients = set()
msg_size = 2048

# Create a function for listening to clients
def handle_client(conn,addr):
    while True:
        # Receive messages and handle exceptions
        try:
            msg = conn.recv(msg_size).decode()
            
            # Iterate over all clients connected and send message
            for cli in clients:
                if cli!=conn:
                    cli.send(msg.encode())

        except Exception:
            conn.close()
            clients.remove(conn)
            print(f"[-]{Fore.RED} {addr[0]}: {addr[1]} disconnected.{Fore.RESET}")
            break


while True:
    # Accepting the client connection
    conn, addr = ssock.accept()
    print(f"[+]{Fore.GREEN} {addr[0]}: {addr[1]} connected.{Fore.RESET}")

    # Add client socket to set
    clients.add(conn)

    # Create a separate thread for the client
    thread = Thread(target=handle_client, args=(conn,addr,))

    # Making the thread daemon, so it ends when the main thread ends
    thread.daemon = True

    # Start the thread
    thread.start()