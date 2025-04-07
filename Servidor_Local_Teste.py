from http.server import HTTPServer, BaseHTTPRequestHandler

class ServidorTeste(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Servidor local rodando. Recebida uma requisicao GET.")


if __name__ == "__main__":
    servidor = HTTPServer(("localhost", 8080), ServidorTeste)
    print("Servidor iniciado em http://localhost:8080")
    servidor.serve_forever()