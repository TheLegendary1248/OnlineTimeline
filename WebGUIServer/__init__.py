from http.server import SimpleHTTPRequestHandler, HTTPServer
PORT = 8000
import os

localonly = True
hostdir = os.path.dirname(os.path.realpath(__file__)) + "/front_src"
class ReqHandler(SimpleHTTPRequestHandler):
    def __init__(self, request, client_address, server, *, directory: str | None = None) -> None:
        print("got request, trying", hostdir)
        super().__init__(request, client_address, server, directory=hostdir)

def main():
    print("Running GUI Main") 
    run()
    return 0 

def run(server_class=HTTPServer, handler_class=ReqHandler):
    server_address = ('127.0.0.1' if localonly else "" , 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == "__main__":
    main()
