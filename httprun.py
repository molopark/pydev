import http.server
import socketserver

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(('',5100), handler) as httpd:
    print('Server run in port 5100...')
    httpd.serve_forever()

