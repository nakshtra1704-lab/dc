from xmlrpc.server import SimpleXMLRPCServer


def increment(value):
    return value + 1


server = SimpleXMLRPCServer(("127.0.0.1", 8002), allow_none=True)
server.register_function(increment, "increment")
print("Stateless server running on port 8002")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nStateless server stopped")
    server.server_close()
