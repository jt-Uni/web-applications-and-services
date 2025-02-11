from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime


class HttpServer(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == '/webapps':
            auth = self.headers['Authorization']

            if auth is None:
                self.send_response(401)
                self.send_header('WWW-Authenticate', 'Basic realm=\"Test\"')
                self.send_header('Content-type', 'text/html')
                self.end_headers()
            else:
                self.send_response(200)
                self.send_header("Content-Type", "text/plain; charset=us-ascii\n")
                self.end_headers()
                self.wfile.write(bytes(str(datetime.now()), "utf-8"))
                user_agent = str(self.headers['User-Agent'])
                self.wfile.write(bytes("Hello User Agent: " + user_agent, "utf-8"))
        else:
            m = "Unsupported URI: " + self.path
            self.send_error(400, m)


httpd = HTTPServer(('localhost', 10000), HttpServer)
httpd.serve_forever()
