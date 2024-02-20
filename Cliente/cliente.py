import socket

# criando o objeto
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost',7777))
print('conectado!!\n')

nameFile =str(input('Arquivo>'))

client.send(nameFile.encode())

#wb:write byte
#abrindo o aqruivo
with open(nameFile,'wb') as file:
   while 1:
      data = client.recv(1000000)
      if not data:
            break
      file.write(data)

      print(f'{nameFile} recebido! \n')