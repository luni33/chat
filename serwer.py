import socket

server_soket = socket . socket (socket .AF_INET , socket.SOCK_STREAM)
server_soket. connect (('localhost',12345))

server_soket.listen(1)
print('Сервер очікує підключення')

connection , adderess = server_soket.accept()
print(f'Підключився клієнт: {adderess}')

date = connection.recv(1024).decode ()
print(f'Отримано повідомленя від клієнта : {date}')

if date =="INFO":
    connection.send('ЦЕ чат від логіки!!'.encode())
elif date =="HELP":
    connection.send('доступно HELP , INFO , HI '.encode())
if date == "HI":
    connection.send('Привіт від сервера !'.encode())
connection.close()
server_soket.close()

