import socket
import requests
import time
from getmac import get_mac_address as gma


def IPs():
    print(f'numero de maquina: {gma()}')  # endereço fisico(MAC)
    ip_local = socket.gethostbyname(socket.gethostname())
    print(f'ip local :         {ip_local}')  # IP local
    ip_publico = requests.get('https://api.ipify.org/').text
    print(f'ip publico:        {ip_publico}')  # IP publico
    time.sleep(60)


IPs()