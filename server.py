import random
import socket

PORT = 9393


def prod(x, g = 3, p = 17):  # Функция просчёта mod
    value = g ** x % p
    return value


with socket.socket() as sock:

    sock.bind(("", PORT))  # Создание сокета
    sock.listen(1)
    print("\nSocket created! Waiting for connecting!\n")
    conn, addr = sock.accept()

    print("Successfully connected from {}\n\n".format(addr[0]))  # Сообщение об успешном подключении, с выводом адреса клиента

    print("{}\n\n".format(conn.recv(1024).decode()))  # Получение приветственного сообщения

    private_key = random.randint(10000, 100000)  # Генерация приватного ключа
    public_c = int(conn.recv(1024).decode())  # Получение публичного ключа клиента
    conn.send(str(prod(x = private_key)).encode())  # Отправка публичного ключа клиенту

    key = prod(g = public_c, x = private_key)  # Просчёт секретного ключа, seed
    print("(key is {})\n".format(key))  # Вывод готового seed, ключа

    random.seed(key)  # Настройка seed

    while True:  # Бесконечный цикл, с получением и расшифровкой сообщения
        encrypted = conn.recv(1024).decode()
        message = ""
        for i, j in zip(range(len(encrypted)), [random.randint(0, 400) for i in range(len(encrypted))]):
            message += chr(ord(encrypted[i]) - j)
        print("encrypted:\t{}\ndecrypted:\t{}\n".format(encrypted, message))
