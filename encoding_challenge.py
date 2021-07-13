#!/bin/python3
#Author:Hussain Saleh
from string import ascii_lowercase as asci
import telnetlib
import json
import base64
HOST = "socket.cryptohack.org"
PORT = 13377

tn = telnetlib.Telnet(HOST, PORT)

def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)

def base(enco):
    result =  base64.b64decode(enco)
    return result

def from_hex(enco):
    return bytearray.fromhex(enco).decode()

def bigint(enco):
    enco = enco[2::]
    return bytearray.fromhex(enco).decode()

def rot13(enco):
    result = ''
    for i in range(len(enco)):
        if enco[i] != '_':
            result += asci[(asci.index(enco[i])-13)%26]
        else:result += enco[i]
    return result
def utf(enco):
    result2 = ''
    for i in enco:
        result2 += chr(int(i))
    return result2
i = 0
while i<=100:
    received = json_recv()
    if i == 100:
        print ("[+] Congratz Here's Your Flag : ",received['flag'])
        break
    if(received['type'] == 'utf-8'):
        result = utf(received['encoded'])
        to_send = {
             "decoded":result.strip()
           }
    elif (received["type"] == "rot13"):
        result = rot13(received['encoded'])
        to_send = {
    "decoded": result.strip()}
    elif (received["type"] == "hex"):
        result = from_hex(received['encoded'])
        to_send = {
    "decoded": result.strip()}
    elif (received["type"] == "bigint"):
        result = bigint(received['encoded'])
        to_send = {
    "decoded": result.strip()}
    elif (received["type"] == "base64"):
        result = base(received['encoded'])
        to_send = {
    "decoded": result.decode().strip()}
#    print("Received type: ")
 #   print(received["type"])
  #  print("Received encoded value: ")
   # print(received["encoded"])
    json_send(to_send)
    print ("Count : " +   str(i))
    i+=1
