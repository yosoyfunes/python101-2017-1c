
import socket

BUFFER_SIZE = 1024

def escucharConexion():

    (clientsocket, address) = serversocket.accept() #Se cuelga aca hasta que alguien se conecte
    print('se conecto', address)

    with clientsocket: #Verifica que dicho cliente siga vivo, mientras escucha.
        while True:
            data = clientsocket.recv(BUFFER_SIZE)
            if data:
                clientsocket.send(data) #ECO DE MENSAJE RECIBIDO
                print(data.decode('UTF-8'))
            else:
                break

    print("se desconecto ", address)

if __name__ == '__main__':
    # crea un socket INET de tipo STREAM
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Esta maquina es", socket.gethostname())
    # asocia el socket a un host publico
    # y a un puerto bien conocido (HTTP = 80)
    serversocket.bind(('0.0.0.0', 80))
    #Si hubiera usado s.bind(('', 80)) or s.bind(('localhost', 80)) or s.bind(('127.0.0.1', 80))
    #tambien tendria un socket servidor, pero solo seria accesible desde la misma maquina.
    # lo convierte en socket servidor TCP
    serversocket.listen(2)

    escucharConexion()
