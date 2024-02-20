import socket

# criando o objeto
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind(('localhost',7777))
print("ouvindo")
servidor.listen(1)

#criando objeto de conexao com cliente
connection, address =servidor.accept()

namefile= connection.recv(1024).decode()

#rb:read byte
with open(namefile,'rb') as file:
    for data in file .readlines():
        connection.send(data)


        print("ARQUIVO ENVIADO!")