# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 08:45:00 2019

@author: 181416
"""
#Bob
import socket
import pickle

def shifr(msg,k):
    rez=''
    for i in range(len(msg)):
        rez+=chr(ord(msg[i])^k)
    return rez   

def send_to_client(conn,msg,k):
    conn.send(pickle.dumps(shifr(msg,k)))
    
def receive_from_client(conn,k):
    msg=shifr(pickle.loads(conn.recv(1024)), k)
    return msg
    
HOST = '127.0.0.1'
PORT = 8083

sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()
b = 2 #секретное число b
msg = conn.recv(1024)
p, g, A = pickle.loads(msg)
B = g**b%p #вычисляем B
print(B)
conn.send(pickle.dumps(B)) #отправляем клиенту
K = A**b%p #генерируем К
print("K:", K)
msg = receive_from_client(conn, K) #получаем число от клиента
print(msg)
send_to_client(conn, K, 'Собщение расшифровано')
conn.close()


