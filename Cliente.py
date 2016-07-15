# -*- coding: iso-8859-1 -*-
from socket import *
import sys
from concurrent.futures import *
#Usar python 3    
class Cliente():
    def __init__(self,nome,host,port):
        self.nome=nome #Recebe o nome do Cliente
        self.host=host #Recebe o ip do computador que será o servidor
        self.port=port #Recebe a porta que vai ser usada
    def conectar(self):
        self.s = socket(AF_INET,SOCK_STREAM) #Cria o socket cliente
        self.s.connect((self.host,self.port)) #Tenta conectar-se ao servidor
        self.s.send(self.nome.encode())
    def escrever(self):#Essa função fica pedindo a mensagem ao cliente em um loop infinito
        while True:
            msg = input(self.nome+":") #Pede a mensagem a ser enviada
            output = (self.nome+":"+msg) #Envia a mensagem junto com o nome de quem enviou
            self.s.send(output.encode())#Envia a mensagem para o servidor
            if msg=="exit()":
                print("Você está saindo da conversa...")
                #self.s.send("%s saiu da conversa")
                self.s.close()
                print("Você saiu da conversa")
                self.s.close()
                break
    def refresh(self):#Essa função verifica se alguem enviou uma mensagem
        while True:
            data = self.s.recv(2048)#Recebe a mensagem enviada pelo servidor
            serv = data.decode("utf8")#Decodifica a mensagem recebido
            print("\n%s" %serv) #Printa a mensagem
        
            

if __name__=="__main__":
    h = "localhost" #Ip do servidor, aqui o servidor é local
    p = 4915 #porta que será usada
    n = input("Qual é o seu nome?\n") #Pega o nome do cliente
    c=Cliente(n,h,p) #Passo informação para a classe Cliente
    c.conectar() # Chama o método que conecta ao servidor
    pool = ThreadPoolExecutor(max_workers=5) #Determina o número de Threads
    pool.submit(c.refresh) #Dá a uma thread a função refresh para ser executada
    pool.submit(c.escrever) #Dá a uma thread a função escrever para ser executada

