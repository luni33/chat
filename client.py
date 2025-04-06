import socket
client_soket = socket . socket(socket .AF_INET, socket.SOCK_STREAM)

client_soket. connect(('tcp://5.tcp.eu.ngrok.io',14467))

msg = input('ведіть повідомленя:  ')
client_soket.send(msg.encode())

response = client_soket.recv(1024).decode()
print(f' Відповідь від сервера: {response}')

client_soket.close()