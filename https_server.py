import http.server
import ssl
import os

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        http.server.SimpleHTTPRequestHandler.end_headers(self)

def main():
    port = 4443
    server_address = ('localhost', port)
    httpd = http.server.HTTPServer(server_address, CORSRequestHandler)

    # Create SSL context
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')

    # Wrap the socket
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

    print(f"Serving HTTPS on https://localhost:{port}")
    httpd.serve_forever()

if __name__ == '__main__':
    main()