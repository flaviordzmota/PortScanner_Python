import socket

ip = input('Digite o host para consulta: ')

ports = []
contador = 0

while contador <  10:
    ports.append(int(input('Informe o n° da porta para verficação: ')))
    contador += 1

for port in ports:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.05)
    code = cliente.connect_ex((ip, port))

    if code == 0:
        print('A porta solicitada n° {} está aberta e disponível.'. format(port))
    else:
        print('A porta solicitada n° {} está fechada.'. format(port))

print('O Scanner foi finalizado, até breve!\n')
