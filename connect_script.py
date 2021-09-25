#!/usr/bin/python3

import socket
import json

HOST, PORT = "socket.cryptohack.org", 11112

socket = socket.socket()

s = socket.connect((HOST, PORT))

data_sent = {
	"buy" : "flag"
}

socket.send(json.dumps(data_sent).encode())

while True:
	json_data = socket.recv(4096).decode()
	print(json_data)
	if "." in json_data:
		break

json_data = socket.recv(4096).decode()
print(json_data)
# print(json.loads(json_data))
