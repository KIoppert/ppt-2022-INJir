import socket
import base64
import json
import os


def Receive():
    data_ = client.recv(2048)
    if data_ == b'EXIT 1' or data_ == b'EXIT 2':
        print('Аварийное завершение программы')
        client.close()
        raise SystemExit
    return data_


def ReadingFile():
    with open('STATES.json', 'r', encoding='utf-8') as f:
        text = json.load(f)
    count = 0
    for i in text.values():
        if count == 2 and i == True:
            Emergency('Достигнута предельная деформация демпфера')
        if count == 1 and i == True:
            Emergency('Нажата кнопка экстренной остановки')
        if count == 0 and i == True:
            pass
        if count == 3:
            if min(i) < 50:
                Emergency('Превышена предельная дистанция дальномера')
        count += 1


def Check():
    client.sendto(b'CIRC_STATE', address)
    data_ = Receive()
    return data_


def Values():
    client.sendto(b'CIRC_ALL_STATE', address)
    f = open('STATES.json', 'wb')
    packet, _ = client.recvfrom(BUFF_SIZE)
    data_ = base64.b64decode(packet, ' /')
    if data_ == b'EXIT 1' or data_ == b'EXIT 2':
        print('Аварийное завершение программы')
        client.close()
        raise SystemExit
    data_.decode('utf-8')
    f.write(data_)
    f.close()
    ReadingFile()


def Emergency(Error):
    # Values()
    while True:
        print('Внимание, нарушение контура безопасности!')
        print(Error)
        client.sendto(b'ALARM', address)
        data_ = Receive()
        if data_ == b'STOPPED':
            break
    return "Safety"


BUFF_SIZE = 65536
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFF_SIZE)

client.settimeout(5)

ipAdr = os.environ['host']
port = os.environ['port']
address = (ipAdr, port)
client.connect(address)
client.sendto(b'INIT_CIRC', address)
print('Подключение...')
try:
    data = Receive()
except TimeoutError:
    print('Не удалось установить подключение')
    client.close()
    raise SystemExit

if data == b'OK':
    print('Установлено подключение к контуру безопасности')
    while True:
        data = Check()
        if data == b"BREAK":
            Values()
        elif data == b'SOLID':
            Values()
    client.close()
    f.close()
