# -*- coding: utf-8 -*-
##################################################################################################################################################################################
##################################################################################################################################################################################

# SerialSocketLibrary

# Desc: biblioteca para a conexão entre o programa e portas via socket ou seriais. Inclui funções de conexão, escrita e recebimento de dados em ambos os casos.
# Functions: serialSocketConnect --> Utilizada para conexão a um socket ou serial.
#            writeSerial --> Função de envio de dados via porta serial.
#            writeSocket --> Função de envio de dados via porta TCP.
#            readSerial --> Função de recebimento de dados via porta serial.
#            readSocket --> Função de recebimento de dados via porta TCP.
# Libraries: serial, serial.tools.list_ports, socket, random.


##################################################################################################################################################################################
##################################################################################################################################################################################
# Import de bibliotecas necessárias


import serial
import serial.tools.list_ports
from socket import *
from random import *
import time



##################################################################################################################################################################################
##################################################################################################################################################################################
# Definição de funções úteis ao código


def serialSocketConnect(cntrl):
   # Desc.: Função utilizada para a conexão do programa com uma porta serial ou com um servidor socket.
   # Return: se a conexão for realizada, retorna a porta serial serialComn ou o socket. Se não, retorna False.
   # Parameters: cntrl -> Se for igual à string "serial", programa conecta-se a uma porta serial.
   #                      Se for igual à string "socket", programa conecta-se a um servidor socket.

   listStrPort = []
   cont = 0

   # Repartição da função destinada à conexão com porta serial

   if cntrl == "serial":

      # Encontra a lista de portas seriais disponíveis e cria outra com os nomes destas

      listPort = serial.tools.list_ports.comports()
      
      for port in listPort:

         listStrPort.append(str(port))

      for n in listStrPort:
                
        print(f"{cont} -> {n}")
                
        cont+=1

      # Informa ao usuário as portas e pede para este escolher
            
      select_port = input("\nSelecione uma porta com base no número: ")

      # Conecta à porta serial, retornando a porta se conseguir e False se não

      try:
      
         serialComn = serial.Serial()

         serialComn.baudrate = 115200

         serialComn.port = listStrPort[int(select_port)][:5]

         serialComn.open()

         print("Sistema conectado à porta serial '%s'. \n" % serialComn.port)

         return serialComn

      except:

         print("Não foi possível conectar à porta desejada...")

         return False
      
   # Repartição destinada para conexão com socket

   elif cntrl == "socket":
      
      tcpPort = int(input("Digite a porta TCP a ser conectada: "))

      host = input("Digite o host a ser conectado: ")

      sock = socket(AF_INET6, SOCK_STREAM)

      try:

         sock.connect((host, tcpPort))

         print("Sistema conectado à porta TCP (%s, %i). \n" % (host, tcpPort))

         return sock

      except:

         print("Não foi possível conectar à porta desejada...")

         return False
      

def writeSerial(serialComn,string):
   # Desc: Função utilizada para enviar uma string por uma porta serial.
   # Return: (-)
   # Parameters: serialComn --> Objeto da classe serial representando uma porta serial conectada.
   #             string --> String a ser enviada.

   serialComn.write(string.encode())

   return


def writeSocket(socket,string):
   # Desc: Função utilizada para enviar uma string por uma porta TCP.
   # Return: (-)
   # Parameters: socket --> Objeto da classe socket representando uma porta TCP conectada.
   #             string --> String a ser enviada

   socket.send(string.encode())

   return


def strReadSerial(cntrl, serialComn, stopByte, numBytes):
   # Desc: Função utilizada para receber uma string por meio de uma porta serial.
   # Return: String a ser recebida.
   # Parameters: cntrol --> Se for igual à string "stopByte", programa limita o recebimento da string por meio de stopByte.
   #                        Se for igual à string "numBytes", programa limita o recebimento da string por meio de numBytes.
   #             serialComn --> Objeto da classe serial representando uma porta serial conectada.
   #             stopByte --> Char determinante para a limitação de recebimento da string.
   #             numBytes --> Valor inteiro determinante para a limitação de recebimento da string.

   string = ""

   # Se cntrl for igual a "stopByte", então recebimento de string é delimitado pelo parâmetro stopByte

   if cntrl == "stopByte":
      
      byteAdd = serialComn.read().decode("utf-8")

      while(byteAdd != stopByte):

        string = string + byteAdd
        byteAdd = serialComn.read().decode("utf-8")

   # Se cntrl for igual a "numBytes", então recebimento de string é delimitado pelo parâmetro numBytes

   elif cntrl == "numBytes":

         string = string + serialComn.read(numBytes).decode("utf-8")

   return string


def strReadSocket(socket, iNumData):
   # Desc: Função utilizada para receber uma string por meio de uma porta TCP.
   # Return: String a ser recebida.
   # Parameters: socket --> Objeto da classe serial representando uma porta serial conectada.

   string = ""

   while(len(string) < iNumData):

      string = string + socket.recv(1024).decode("utf-8")


   return string


      
