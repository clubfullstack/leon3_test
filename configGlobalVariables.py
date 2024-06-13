# -*- coding: utf-8 -*-
##################################################################################################################################################################################
##################################################################################################################################################################################

# configGlobalVariables.py

# Desc: Biblioteca destinada à configuração de variáveis globais para a realização de testes de comunicação inter UARTs.
# Functions: readStrCntrl --> Função de leitura da variável global strCntrl.
#            setStrCntrl --> Função de mudança da variável global strCntrl.
#            readStrData --> Função de leitura da variável global strData.
#            setStrData --> Função de mudança da variável global strData.
#            setITime --> Função de mudança da variável global iTime.
#            readITime --> Função de leitura da variável global iTime.
#            readOConfig --> Função de leitura da variável global oConfig.
#            setOConfig --> Função de mudança da variável global oConfig.
#            setIContTest --> Função de mudança da variável global iContTest.
#            readIContTest --> Função de leitura da variável global iContTest.
#            initOFile --> Função de inicialização do arquivo de log.
#            appendOFile --> Função de adição de linha ao arquivo de log.
#            closeOFile --> Função de fechamento do arquivo de log.
# Libraries: -


##################################################################################################################################################################################
##################################################################################################################################################################################
# Declaração das variáveis globais

strCntrl = ""
strData = ""
iContTest = 0
iTime = 0
oConfig = {"iNumTest" : 0, "iNumOffset" : 0, "iNumData": 0}
oFile = 0

##################################################################################################################################################################################
##################################################################################################################################################################################
# Funções de leitura e mudança das variáveis globais

def readStrCntrl():
   # Desc: Função de leitura da variável global strCntrl.
   # Return: (strCntrl) --> Variável global de controle de ação.
   # Parameters: (-)
   
   global strCntrl

   return strCntrl

def setStrCntrl(string):
   # Desc: Função de mudança da variável global strCntrl.
   # Return: (-)
   # Parameters: (string) --> Variável global de controle de ação.

   global strCntrl

   strCntrl = string

def readStrData():
   # Desc: Função de leitura da variável global strData.
   # Return: (strData) --> Variável global de transferência de dados.
   # Parameters: (-)

   global strData

   return strData

def setStrData(string):
   # Desc: Função de mudança da variável global strData.
   # Return: (-)
   # Parameters: (string) --> Variável global de transferência de dados.

   global strData

   strData = string

def setITime(time):
   # Desc: Função de mudança da variável global iTime.
   # Return: (-)
   # Parameters: (time) --> Variável global de tempo.

   global iTime

   iTime = time

def readITime():
   # Desc: Função de leitura da variável global iTime.
   # Return: (iTime) --> Variável global de tempo.
   # Parameters: (-)

   global iTime

   return iTime

def readOConfig():
   # Desc: Função de leitura da variável global oConfig.
   # Return: (oConfig) --> Variável global de configuração.
   # Parameters: (-)

   global oConfig

   return oConfig

def setOConfig(dicionario):
   # Desc: Função de mudança da variável global oConfig.
   # Return: (-)
   # Parameters: (dicionario) --> Variável global de configuração.

   global oConfig

   oConfig = dicionario

def setIContTest(cont):
   # Desc: Função de mudança da variável global iContTest.
   # Return: (-)
   # Parameters: (cont) --> Variável global de controle de teste.

   global iContTest

   iContTest = cont

def readIContTest():
   # Desc: Função de leitura da variável global iContTest.
   # Return: (iContTest) --> Variável global de controle de teste.
   # Parameters: (-)

   global iContTest

   return iContTest

def initOFile():
   # Desc: Função de inicialização do arquivo de log.
   # Return: (-)
   # Parameters: (-)

    global oFile

    oFile = open("textLog.csv", "w")
    oFile.write("id,strCommunication,strOperation,strData,fTime,iOffset,iNumData,bResult\n")

    return oFile

def appendOFile(string):
   # Desc: Função de adição de linha ao arquivo de log.
   # Return: (-)
   # Parameters: (string) --> String a ser adicionada ao arquivo de log.

    global oFile

    oFile.write(string)

def closeOFile():
   # Desc: Função de fechamento do arquivo de log.
   # Return: (-)
   # Parameters: (-)

   global oFile

   oFile.close()







