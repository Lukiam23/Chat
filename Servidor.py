#Instalar bluelet
import bluelet
#Use python 3
def echoer(conn):
    contas.append(conn)#Coloca a conexão em uma lista
    nome = yield conn.recv(1024)
    nomes.append(nome.decode('utf8'))
    mensagem = "%s conectou-se ao servidor" %nome.decode('utf8')
    for i in contas:#Pecorrer a lista contas
        if i!=conn:#Se i for diferente da minha conta
            yield i.sendall(mensagem.encode())#Envia para todos na lista contas menos para mim
    while True:
        data = yield conn.recv(1024)#pega dado da conexão
        if not data:
            break
        for n in nomes:#Pecorre a lista nomes
            comp="%s:exit()"%n#Irá servir como base para comparar
            if comp==data.decode('utf8'):#Se a mensagem em data for igual a "nome da pessoa: exit()" 
                nomes.remove(n)#Se remove o nome de quem enviou da lista nomes
                contas.remove(conn)#Remove o conn de quem enviou da lista contas
                resposta ="%s saiu da conversa" %n#Resposta que será enviada aos clientes conectados 
                data = resposta.encode()
        for n in nomes:
            commandWhoIsOn = "%s:Who is on?" %n
            if commandWhoIsOn==data.decode('utf8'):
                data=b''
                for userOn in nomes:
                    who ="%s está online" %userOn
                    yield conn.sendall(who.encode())
                    
        for i in contas:#Vai pegar todas as conexões que estão na lista contas
            if i!=conn:#Se "i" for diferente da conexão que está enviando a mensagem
                yield i.sendall(data)#envia a mensagem para as outra conexões
		
contas=[]
nomes=[]
if __name__=="__main__":
    print("Servidor Rodando...")
    bluelet.run(bluelet.server('', 4915, echoer))
