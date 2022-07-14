import http.server
import socketserver

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(('',5000), handler) as httpd:
    print('Server run in port 5000...')
    httpd.serve_forever()

