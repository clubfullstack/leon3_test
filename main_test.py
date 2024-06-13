# -*- coding: utf-8 -*-
##################################################################################################################################################################################
##################################################################################################################################################################################

# main_test.py

# Desc: programa principal utilizado na execução das threads definidas em modulatedTestLibrary, passo final para a execução dos testes
# Libraries: modulatedTestLibrary (e afins), threading.


##################################################################################################################################################################################
##################################################################################################################################################################################

# Import de bibliotecas necessárias

from modulatedTestLibrary import *
import threading
from configGlobalVariables import *

import socket

##################################################################################################################################################################################
##################################################################################################################################################################################
# Configurações iniciais do teste

# Inicialização da variável global de controle de ação
setStrCntrl("start")

# Inicialização da variável global de transferência de dados
ArrayComn = oCicleInit()

# Instanciação das threads responsávies pela comunicação e validação dos testes
thread1 = threading.Thread(target = IOWork, args = [ArrayComn])
thread2 = threading.Thread(target = TestMaker)

# Inicialização das threads
thread1.start()
thread2.start()

# Conecte-se ao container QEMU na porta 5050 usando o nome do serviço definido no docker-compose.yml
def main():
    HOST = 'qemu-emulator'
    PORT = 5050

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            # Lógica de comunicação aqui
            s.sendall(b'Hello, QEMU!')
            data = s.recv(1024)
            print('Received', repr(data))
    except ConnectionRefusedError:
        print("Could not connect to QEMU emulator. Is it running and accessible?")

if __name__ == "__main__":
    main()


