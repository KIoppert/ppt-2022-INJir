import socket
import os

BUFF_SIZE = 65536
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFF_SIZE)


ipAdr = os.environ['host']
port = os.environ['port']
address = (ipAdr, int(port))
client.connect(address)

client.sendto(b'YOUNG_INIT', address)
data_ = client.recv(2048)
if data_ == b'YOUNG_START':
    client.sendto(b'YOUNG_HOME', address)

    client.sendto(b'YOUNG_LMOVE:25.113:0.463:8.15:', address)
    client.sendto(b'GLUE_PUMP_ON', address)

    client.sendto(b'YOUNG_DRAW:0:8.868:0:', address)
    client.sendto(b'YOUNG_DRAW:-0.807:5.242:0:', address)
    client.sendto(b'YOUNG_DRAW:-2.347:4.756:0:', address)
    client.sendto(b'YOUNG_DRAW:-3.67:3.829:0:', address)
    client.sendto(b'YOUNG_DRAW:-4.652:2.547:0:', address)
    client.sendto(b'YOUNG_DRAW:-5.203:1.029:0:', address)

    client.sendto(b'YOUNG_DRAW:-4.263:0.617:0:', address)
    client.sendto(b'YOUNG_DRAW:-4.052:1.463:0:', address)
    client.sendto(b'YOUNG_DRAW:-3.674:2.248:0:', address)
    client.sendto(b'YOUNG_DRAW:-3.147:2.941:0:', address)
    client.sendto(b'YOUNG_DRAW:-2.491:3.514:0:', address)
    client.sendto(b'YOUNG_DRAW:-1.733:3.944:0:', address)

    client.sendto(b'YOUNG_DRAW:-1.586:3.573:0:', address)
    client.sendto(b'YOUNG_DRAW:-2.33:3.139:0:', address)
    client.sendto(b'YOUNG_DRAW:-3.032:2.467:0:', address)
    client.sendto(b'YOUNG_DRAW:-3.55:1.636:0:', address)
    client.sendto(b'YOUNG_DRAW:-3.781:0.994:0:', address)
    client.sendto(b'YOUNG_DRAW:-2.875:0.253:0:', address)

    client.sendto(b'YOUNG_DRAW:-17.591:0:0:', address)
    client.sendto(b'YOUNG_DRAW:-0.707:-0.293:0:', address)
    client.sendto(b'YOUNG_DRAW:-0.293:-0.707:0:', address)

    client.sendto(b'YOUNG_DRAW:0:-4:0:', address)

    client.sendto(b'YOUNG_DRAW:0.293:-0.707:0:', address)
    client.sendto(b'YOUNG_DRAW:0.707:-0.293:0:', address)

    client.sendto(b'YOUNG_DRAW:10:0:0:', address)

    client.sendto(b'YOUNG_DRAW:0.707:-0.293:0:', address)
    client.sendto(b'YOUNG_DRAW:0.293:-0.707:0:', address)

    client.sendto(b'YOUNG_DRAW:0:-12:0:', address)

    client.sendto(b'YOUNG_DRAW:-0.293:-0.707:0:', address)
    client.sendto(b'YOUNG_DRAW:-0.707:-0.293:0:', address)

    client.sendto(b'YOUNG_DRAW:-10:0:0:', address)

    client.sendto(b'YOUNG_DRAW:-0.707:-0.293:0:', address)
    client.sendto(b'YOUNG_DRAW:-0.293:-0.707:0:', address)

    client.sendto(b'YOUNG_DRAW:0:-4:0:', address)

    client.sendto(b'YOUNG_DRAW:0.293:-0.707:0:', address)
    client.sendto(b'YOUNG_DRAW:0.707:-0.293:0:', address)

    client.sendto(b'YOUNG_DRAW:10:0:0:', address)

    client.sendto(b'YOUNG_DRAW:0.707:-0.293:0:', address)
    client.sendto(b'YOUNG_DRAW:0.293:-0.707:0:', address)

    client.sendto(b'YOUNG_DRAW:0:-12:0:', address)

    client.sendto(b'YOUNG_DRAW:-0.293:-0.707:0:', address)
    client.sendto(b'YOUNG_DRAW:-0.707:-0.293:0:', address)

    client.sendto(b'YOUNG_DRAW:-10:0:0:', address)

    client.sendto(b'YOUNG_DRAW:-0.707:-0.293:0:', address)
    client.sendto(b'YOUNG_DRAW:-0.293:-0.707:0:', address)

    client.sendto(b'YOUNG_DRAW:0:-4:0:', address)

    client.sendto(b'YOUNG_DRAW:0.293:-0.707:0:', address)
    client.sendto(b'YOUNG_DRAW:0.707:-0.293:0:', address)

    client.sendto(b'YOUNG_DRAW:10:0:0:', address)

    client.sendto(b'YOUNG_DRAW:0.707:-0.293:0:', address)
    client.sendto(b'YOUNG_DRAW:0.293:-0.707:0:', address)

    client.sendto(b'YOUNG_DRAW:0:-12:0:', address)

    client.sendto(b'YOUNG_DRAW:-0.293:-0.707:0:', address)
    client.sendto(b'YOUNG_DRAW:-0.707:-0.293:0:', address)

    client.sendto(b'YOUNG_DRAW:-10:0:0:', address)

    client.sendto(b'YOUNG_DRAW:-0.707:-0.293:0:', address)
    client.sendto(b'YOUNG_DRAW:-0.293:-0.707:0:', address)

    client.sendto(b'YOUNG_DRAW:0:-4:0:', address)

    client.sendto(b'YOUNG_DRAW:0.293:-0.707:0:', address)
    client.sendto(b'YOUNG_DRAW:0.707:-0.293:0:', address)

    client.sendto(b'YOUNG_DRAW:10:0:0:', address)

    client.sendto(b'YOUNG_DRAW:0.707:-0.293:0:', address)
    client.sendto(b'YOUNG_DRAW:0.293:-0.707:0:', address)

    client.sendto(b'YOUNG_DRAW:0:-12:0:', address)

    client.sendto(b'YOUNG_DRAW:-0.293:-0.707:0:', address)
    client.sendto(b'YOUNG_DRAW:-0.707:-0.293:0:', address)

    client.sendto(b'YOUNG_DRAW:-10:0:0:', address)

    client.sendto(b'YOUNG_DRAW:-0.707:-0.293:0:', address)
    client.sendto(b'YOUNG_DRAW:-0.293:-0.707:0:', address)

    client.sendto(b'YOUNG_DRAW:0:-4:0:', address)

    client.sendto(b'YOUNG_DRAW:0.293:-0.707:0:', address)
    client.sendto(b'YOUNG_DRAW:0.707:-0.293:0:', address)

    client.sendto(b'YOUNG_DRAW:10:0:0:', address)

    client.sendto(b'YOUNG_DRAW:0.707:-0.293:0:', address)
    client.sendto(b'YOUNG_DRAW:0.293:-0.707:0:', address)

    client.sendto(b'YOUNG_DRAW:0:-8:0:', address)

    client.sendto(b'YOUNG_DRAW:0.293:-0.707:0:', address)
    client.sendto(b'YOUNG_DRAW:0.707:-0.293:0:', address)

    client.sendto(b'YOUNG_DRAW:15.845:0:0:', address)

    client.sendto(b'YOUNG_DRAW:2.984:-0.214:0:', address)
    client.sendto(b'YOUNG_DRAW:2.921:-0.65:0:', address)
    client.sendto(b'YOUNG_DRAW:2.787:-1.088:0:', address)
    client.sendto(b'YOUNG_DRAW:2.61:-1.463:0:', address)
    client.sendto(b'YOUNG_DRAW:1.816:-1.248:0:', address)
    client.sendto(b'YOUNG_DRAW:1.654:-1.456:0:', address)

    client.sendto(b'YOUNG_DRAW:1.604:-1.604:0:', address)

    client.sendto(b'YOUNG_DRAW:0.649:-0.434:0:', address)
    client.sendto(b'YOUNG_DRAW:0.765:-0.152:0:', address)

    client.sendto(b'YOUNG_DRAW:1.281:0:0:', address)

    client.sendto(b'YOUNG_DRAW:0.765:0.152:0:', address)
    client.sendto(b'YOUNG_DRAW:0.649:0.434:0:', address)

    client.sendto(b'YOUNG_DRAW:30.176:30.176:0:', address)

    client.sendto(b'YOUNG_DRAW:0.434:0.649:0:', address)
    client.sendto(b'YOUNG_DRAW:0.152:0.765:0:', address)

    client.sendto(b'YOUNG_DRAW:0:1.426:0:', address)

    client.sendto(b'YOUNG_DRAW:-0.191:0.852:0:', address)
    client.sendto(b'YOUNG_DRAW:-0.535:0.69:0:', address)

    client.sendto(b'YOUNG_DRAW:-1.915:1.796:0:', address)
    client.sendto(b'YOUNG_DRAW:-1.674:2.022:0:', address)
    client.sendto(b'YOUNG_DRAW:-1.407:2.216:0:', address)
    client.sendto(b'YOUNG_DRAW:-1.118:2.375:0:', address)
    client.sendto(b'YOUNG_DRAW:-0.812:2.497:0:', address)
    client.sendto(b'YOUNG_DRAW:-0.492:2.579:0:', address)
    client.sendto(b'YOUNG_DRAW:-0.165:2.62:0:', address)

    client.sendto(b'GLUE_PUMP_OFF', address)
    client.sendto(b'YOUNG_HOME', address)
    client.sendto(b'YOUNG_DISCONNECT', address)
