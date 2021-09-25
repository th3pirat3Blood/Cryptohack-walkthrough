#!/usr/bin/python3

import socket
import json
import base64
import codecs

def decode_data(data, etype):
	d_data = ""
	
	if etype == "base64":
		d_data = base64.b64decode(data).decode()

	elif etype == "hex":
		d_data = bytearray.fromhex(data).decode()

	elif etype == "rot13":
		d_data = codecs.decode(data, "rot13")

	elif etype == "bigint":
		d_data = bytearray.fromhex(data[2:]).decode()

	elif etype == "utf-8":
		d_data = "".join([chr(f) for f in data])

	return d_data


HOST, PORT = "socket.cryptohack.org", 13377
sample_data = {"type": "bigint", "encoded": "0x636f6d706c6574655f6368656d6963616c5f636f756e7479"}
sample_error = {'error': 'Decoding fail'}

socket = socket.socket()
s = socket.connect((HOST, PORT))

for i in range(100):
	json_data = socket.recv(4096).decode()
	recv_data = json.loads(json_data)
	print(f"{i} : {recv_data}")

	if "type" in recv_data:
		encoding_type = recv_data["type"]
		encoded_data = recv_data["encoded"]
	else:
		print("ERROR")
		exit(0)
	# print(f"{encoded_data}\t{encoding_type}")

	decoded_value = decode_data(encoded_data, encoding_type)
	data_to_send = {
		"decoded" : decoded_value
	}
	print(decoded_value)
	socket.send(json.dumps(data_to_send).encode())

json_data = socket.recv(4096).decode()
recv_data =json.loads(json_data)
print("\n\nFLAG: ", recv_data)