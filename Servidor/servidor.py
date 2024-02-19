import socket

# criando o objeto
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind(('localhost','7777'))
servidor.listen(1)

connection, address =servidor.accept()

namefile= connection.recv(1024).decode()

with open(namefile,'rb') as file:
    for data in file .readlines():
        connection.send(data)