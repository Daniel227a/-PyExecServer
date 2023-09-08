import socket

class active_clients:
    
        def __init__(self,host,port):
            self.host = host
            self.port = port

def handle_client(client_socket):
    # Receber o conteúdo do arquivo do cliente
    file_content = client_socket.recv(4096)

    # Salvando o conteúdo do arquivo em um arquivo temporário
    with open("temp_script.py", "wb") as temp_file:
        temp_file.write(file_content)

    try:
        # Executar o código do arquivo temporário
        exec(compile(file_content, "temp_script.py", 'exec'))
        client_socket.send("Execução bem sucedida.".encode())
    except Exception as e:
        # Enviar a mensagem de erro para o cliente
        client_socket.send(str(e).encode())

    client_socket.close()

def main():
    host = "0.0.0.0"  # Aceitar conexões em qualquer endereço IP da máquina
    port = 90

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print("[*] Servidor ouvindo em {}:{}".format(host, port))

    while True:
        client_socket, addr = server_socket.accept()
        #print("[*] Conexão aceita de {}:{}".format(addr[0], addr[1]))
        cliente=active_clients(addr[0], addr[1])
        print("Conexão aceita de {}:{}".format(cliente.host,cliente.port))
        handle_client(client_socket)

if __name__ == "__main__":
    main()
    