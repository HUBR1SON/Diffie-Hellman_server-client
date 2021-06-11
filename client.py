import random
import socket

PORT = 9393


def prod(x, g = 3, p = 17):  # Функция просчёта mod
    value = g ** x % p
    return value


with socket.socket() as sock:

    sock.connect(("localhost", PORT))  # Подключение  к серверу
    sock.send("<----------- I'm here! ----------->".encode())  # Отправка приветственного сообщения

    private_key = random.randint(10000, 100000)  # Генерация приватного ключа
    sock.send(str(prod(x = private_key)).encode())  # Отправка публичного ключа серверу
    public_s = int(sock.recv(1024).decode())  # Получение публичного ключа сервера

    key = prod(g = public_s, x = private_key)  # Просчёт секретного ключа, seed
    print("(key is {})".format(key))  # Вывод готового seed, ключа

    random.seed(key)  # Настройка seed

    while True:  # Бесконечный цикл с отправкой шифрованных сообщений
        message = input()
        encrypted = ""
        for i, j in zip(range(len(message)), [random.randint(0, 400) for i in range(len(message))]):
            encrypted +=  chr(ord(message[i]) + j)
        print("encrypted sended:\t{}\n".format(encrypted))
        sock.send(encrypted.encode())
