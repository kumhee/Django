from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response_only(200, 'OK')
        self.send_header('Content-Type', 'Text.plain')
        self.end_headers()
        self.wfile.write(b"Hello World")

if __name__ == "__main__":
    server = HTTPServer(('', 8888), MyHandler)
    print("Started WebServer on port 8888....")
    print("Precc ^C to quite Webserver.")
    server.serve_forever()