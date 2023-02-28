import socket
import time

HOST='192.168.50.232'
PORT=9999

s_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

print('server open')

s_socket.bind((HOST,PORT))
s_socket.listen()
c_socket,addr = s_socket.accept()
print('Connected by', addr)


while True:
    
    data = c_socket.recv(1024)


    if not data:         
         break
      
    print(data.decode())


    



 
       

    

    
