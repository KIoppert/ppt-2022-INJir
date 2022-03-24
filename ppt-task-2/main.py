from socket import *
import json

def Connect():
    client_socket.sendto(b'INIT_CIRC', socket_address)
    data_ = socket.recv()
    data_ = bytes.decode(data_)
    data_ = client_socket.recvfrom(1024)
    return data_

def Check_Status():
    client_socket.sendto(b'CIRC_STATE', socket_address)
    data_ = socket.recv()
    data_ = bytes.decode(data_)
    data_ = client_socket.recvfrom(1024)
    return data_

def Emergency():
    client_socket.sendto(b'ALARM', socket_address)
    data_ = socket.recv()
    data_ = bytes.decode(data_)
    data_ = client_socket.recvfrom(1024)
    Values()
    if data_ == 'STOPPED':
        return 'Exit'

def Values():
    client_socket.sendto(b'CIRC_ALL_STATE', socket_address)
    status = open('STATE.json')
    data_ = socket.recv()
    data_ = bytes.decode(data_)
    data_ = client_socket.recvfrom(1024)
    status.write(data_)
    with open('STATE.json', 'r', encoding='utf8') as f:
        text = f.read()
    stat = json.loads(text)
    for i, k in stat.items():
        if i == 'state' and k == 'false ':
            return 'Контур разомкнут'
        if i == 'ebutton' and k == 'true':
            return 'Нажата кнопка экстренной остановки'
        if i == 'end_cap' and k == 'true':
            return 'Достигнута предельная деформация демпфера'
        if i == 'dist' and min(k) < 50:
            return 'Превышена предельная дистанция дальномера'
        return data_

def Break():
    print('Не удалось установить подключение')

host = '127.0.0.1'
port = 80


socket_address = (host, port)

BUFF_SIZE = 65536
client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
client_socket.bind(socket_address)

try:
    data = Connect()
except client_socket.timeout(5):
    Break()
if data == 'OK':
    client_socket.send('Установлено подключение к контуру безопасности')
    while True:
        data = Check_Status()

        if data == 'SOLID':
            pass

        elif data == 'BREAK':
            while True:
                code = Emergency()

                if code == 'Exit':
                    break
        Values()
