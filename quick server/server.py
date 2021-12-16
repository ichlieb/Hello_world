import socket
import reply
import andrpack as pack

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
sock.bind(('', 8080))  # связываем сокет с портом, где он будет ожидать сообщения
sock.listen(10)  # указываем сколько может сокет принимать соединений
print('Server is running, please, press ctrl+c to stop')
while True:
    conn, addr = sock.accept()  # начинаем принимать соединения
    print('connected:', addr)  # выводим информацию о подключении
    data = pack.int_from_bytes(conn.recv(4))
    if (data == 1): 
        print("Handling Suggestion")
        reply.suggestion(conn)
    elif (data == 2):
        print("Handling Search")
        reply.find_person(conn)
    print("Handled")
conn.close()  # закрываем соединение