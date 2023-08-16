# coding:utf-8
import http.server
import socketserver

port = 8000
adress = ("", port)

handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(adress, handler)

print(f"Serveur démarré avec succes sur le port {port}")

httpd.serve_forever()
