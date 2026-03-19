import socket
import os

# Railway asigna el puerto automáticamente en la variable PORT
PORT = int(os.environ.get("PORT", 42124))

def start_server():
    # Creamos el socket TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Permitir reutilizar la dirección si el servidor se reinicia
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server.bind(('0.0.0.0', PORT))
        server.listen(5)
        print("[*] Servidor FIFA Bypass activo en puerto {0}".format(PORT))
    except Exception as e:
        print("[!] Error al iniciar: {0}".format(e))
        return

    while True:
        try:
            client, addr = server.accept()
            print("[+] Conexion recibida de {0}".format(addr))
            
            # El código hexadecimal que engaña al servidor de EA
            # Corresponde a un login exitoso (Bypass)
            response = bytes.fromhex("000000010000000000000000")
            
            # Enviamos la respuesta y cerramos
            client.sendall(response)
            client.close()
        except Exception as e:
            print("[!] Error durante la conexion: {0}".format(e))

if __name__ == "__main__":
    start_server()
