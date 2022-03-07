"""
This is an implementation of client with sockets for chat room
The Colorama module is used to colorize the text in prompt. 

> Author: Team-3
"""

# import necessary libraries
import socket, sys, random
from threading import Thread
from colorama import Fore, Back, Style, init

# Initialize to print out colors in cmd prompt
init(convert=True)

# List of colors
color = [Fore.BLUE, Fore.CYAN, Fore.MAGENTA, Fore.LIGHTGREEN_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.YELLOW]

# Choose a random color for each user
cli_color = random.choice(color)

# We are using TCP protocol
csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# server's host address for the client to connect
host = socket.gethostname()
port = 5000

# bind the socket to the address
csock.connect((host, port))

print(f"\n{Back.BLUE}========================= Welcome to ChatRoom :) ========================{Style.RESET_ALL}\n")
print(f"[+]{Fore.GREEN} Connected to server at {host}:{port}{Fore.RESET}")

# Get the client's name
try:
    print(f"[*] {Fore.GREEN}Enter your name: {Fore.RESET}",end="")
    name = input()
    csock.send(f"{Style.BRIGHT}{cli_color}{name}{Fore.RESET} ENTERED THE CHATROOM...{Style.RESET_ALL}".encode())

except KeyboardInterrupt:
    print(f"\n{Fore.GREEN}EXITING THE CHATROOM...{Fore.RESET}")
    csock.close()
    sys.exit()

# Handle the incoming messages
def handle_messages():
    while True:
        try:
            message = csock.recv(1024).decode()
        except:
            break

        print("\r"+message)
        print(f"{cli_color}{Style.BRIGHT}You: {Style.RESET_ALL}", end="")

# Create a thread for handling incoming msgs
t = Thread(target=handle_messages)

# Making the thread daemon, so it ends when the main thread ends
t.daemon = True

# Start the thread
t.start()

print(f"{Fore.LIGHTRED_EX}\nTo exit the chatroom type q() and Enter\n{Fore.RESET}")

# Continuously get input from the client
while True:
    try:
        print(f"{cli_color}{Style.BRIGHT}You: {Style.RESET_ALL}", end="")
        msg = input()

        # If entered q() then quit
        if msg == 'q()':
            csock.send(f"{Style.BRIGHT}{cli_color}{name}{Fore.RESET} LEFT THE CHATROOOM...{Style.RESET_ALL}".encode())
            print(f"{Fore.GREEN}\nEXITING THE CHATROOM...{Fore.RESET}")
            break

        # If msg is empty then don't send
        elif msg.strip()=="":
            continue

        msg = f"{cli_color}{Style.BRIGHT}{name}{Style.RESET_ALL}: {msg}"
        csock.send(msg.encode())

    # In-case if ctrl+c is pressed, then exit
    except KeyboardInterrupt:
        csock.send(f"{Style.BRIGHT}{cli_color}{name}{Fore.RESET} LEFT THE CHATROOOM...{Style.RESET_ALL}".encode())
        print(f"{Fore.GREEN}\nEXITING THE CHATROOM...{Fore.RESET}")
        break

csock.close()