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
