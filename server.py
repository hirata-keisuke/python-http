import http.server
from urllib.parse import urlparse, parse_qs

PORT = 8000

class MyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        print(f"path={self.path}")

        parsed_path = urlparse(self.path)
        print(f"parsed path={parsed_path}")
        print(f"query={parse_qs(parsed_path)}")

        print('headers\r\n-----\r\n{}-----'.format(self.headers))

        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(b'Hello from do_GET')

    def do_POST(self):
        print('path = {}'.format(self.path))

        parsed_path = urlparse(self.path)
        print('parsed: path = {}, query = {}'.format(parsed_path.path, parse_qs(parsed_path.query)))

        print('headers\r\n-----\r\n{}-----'.format(self.headers))

        content_length = int(self.headers['content-length'])

        print('body = {}'.format(self.rfile.read(content_length).decode('utf-8')))

        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(b'Hello from do_POST')


with http.server.HTTPServer(("", PORT), MyHTTPRequestHandler) as httpd:

    print(f"serving at port{PORT}")
    httpd.serve_forever()
