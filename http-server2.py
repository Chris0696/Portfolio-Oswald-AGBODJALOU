# coding:utf-8
import http.server


port = 8002
adress = ("", port)

server = http.server.HTTPServer

handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]

httpd = server(adress, handler)

print(f"Serveur démarré avec succes sur le port {port}")

httpd.serve_forever()
