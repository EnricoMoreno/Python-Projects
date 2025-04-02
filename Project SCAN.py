import socket
import threading

port_services = {
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP"
}


def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  
        result = sock.connect_ex((ip, port))  

        if result == 0:
            service = port_services.get(port, "Desconhecido")
            print(f"Porta {port} está aberta! Serviço: {service}")

        sock.close()

    except Exception as e:
        print(f"Erro ao escanear porta {port}: {e}")

def scan_ports(ip, ports):
    threads = []

    for port in ports:
        thread = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    target_ip = input("Digite o IP alvo: ")
    port_range = range(1, 1025) 

    print(f"Escaneando {target_ip}...\n")
    scan_ports(target_ip, port_range)
    print("\nEscaneamento concluído!")