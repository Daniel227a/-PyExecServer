import socket
import tkinter as tk
from tkinter import filedialog

def send_file(file_content):
    host = "0.0.0.0"
    
    port = 90

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Enviar o conteúdo do arquivo para o servidor
    client_socket.send(file_content)

    # Receber o resultado da execução do servidor
    result = client_socket.recv(1024).decode()

    print("Resultado da execução:")
    print(result)

    client_socket.close()

def choose_file():
    root = tk.Tk()
    root.withdraw()  # Ocultar a janela principal

    # Abrir janela de diálogo para seleção do arquivo
    file_path = filedialog.askopenfilename()

    if file_path:
        with open(file_path, "rb") as file:
            file_content = file.read()
        send_file(file_content)
    else:
        print("Nenhum arquivo selecionado.")

if __name__ == "__main__":
    choose_file()
