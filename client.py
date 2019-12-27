# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 08:44:13 2019

@author: 181416
"""
#ALICE
import socket
import pickle

def shifr(msg,k):
    rez=''
    for i in range(len(msg)):
        rez+=chr(ord(msg[i])^k)
    return rez
    
def send_to_server(conn,msg,k):
    conn.send(pickle.dumps(shifr(msg,k)))
    
def receive_from_server(conn,k):
    msg=shifr(pickle.loads(conn.recv(1024)), k)
    return msg
    

HOST = '127.0.0.1'
PORT = 8083

sock = socket.socket()
sock.connect((HOST, PORT))
p, g, a = 7, 5, 3
A = g**a%p #генерируем A
print(A)
sock.send(pickle.dumps((p, g, A))) #отправляем на сервер
B=pickle.loads(sock.recv(1024))
K=B**a%p #генерируем K
print("K:", K)
msg='Hello!'
send_to_server(sock, msg, K) #отправляем клиенту K
print(' ' + receive_from_server(sock, K))
sock.close()



