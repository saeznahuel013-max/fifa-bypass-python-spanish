import socket
import os

# Railway usa la variable PORT automáticamente
PORT = int(os.environ.get("PORT", 42124))

def start_server():
    # Usamos TCP para que la PS3 no se pierda
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', PORT))
    server.listen(5)
    print("[*] Servidor Python activo en puerto {0}".format(PORT))

    while True:
        try:
            client, addr = server.accept()
            print("[+] Conexion recibida de {0}".format(addr))
            
            # El código mágico de login (bypass)
            response = bytes.fromhex("000000010000000000000000")
            client.sendall(response)
            client.close()
        except Exception as e:
            print("[!] Error: {0}".format(e))

if __name__ == "__main__":
    start_server()
