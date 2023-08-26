import http.server
import socketserver

# Especifique o diretório que você deseja servir
directory = r'C:\\Users\\Edicarlos\\Dropbox\\Projects\\Comercial-Simplific\\novo-site'

# Escolha a porta em que o servidor vai escutar
port = 8000

# Crie o servidor web
handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", port), handler)

print(f"Serving at port {port}")
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.shutdown()
    print("\nServer stopped.")
