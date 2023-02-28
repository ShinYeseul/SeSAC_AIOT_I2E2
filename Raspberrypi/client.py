import time
import socket

HOST='192.168.50.232' # server address
PORT=9999

c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c_socket.connect((HOST,PORT))
print('connected!')