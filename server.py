import imp


import os
try:
    from SimpleHTTPServer import SimpleHTTPRequestHandler as Handler
    from SocketServer import TCPServer as Server
except:
    from http.server import SimpleHTTPRequestHandler as Handler
    from http.server import HTTPServer as Server
    
PORT = int(os.getenv('PORT', 8001))
os.chdir('static')

httpd = Server(("", PORT), Handler)
try:
    print("Starting serving at port %i" % PORT)
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
httpd.server_close()