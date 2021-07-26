from http.server import HTTPServer, SimpleHTTPRequestHandler
server = HTTPServer(('0.0.0.0', 8002), SimpleHTTPRequestHandler)
server.serve_forever()
