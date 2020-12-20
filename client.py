import random
import socket
from DHP import *


PORT = 9393

with socket.socket() as sock:

    sock.connect(("localhost", PORT))  # Подключение  к серверу
    sock.send("<----------- I'm here! ----------->".encode())  # Отправка приветственного сообщения

    private_key = random.randint(10000, 100000)  # Генерация приватного ключа
    sock.send(str(prod(x = private_key)).encode())  # Отправляет публичный ключ серверу
    public_s = int(sock.recv(1024).decode())  # Получает публичный ключ сервера

    key = prod(g = public_s, x = private_key)  # Просчитывает секретный ключ, seed
    print("(key is {})".format(key))  # Выводит готовый seed, ключ

    random.seed(key)  # Настраиваем seed

    while True:  # Бесконечный цикл с отправкой шифрованных сообщений
        message = input()
        encrypted = ""
        for i, j in zip(range(len(message)), [random.randint(0, 400) for i in range(len(message))]):
            encrypted +=  chr(ord(message[i]) + j)
        print("encrypted sended:\t{}\n".format(encrypted))
        sock.send(encrypted.encode())
