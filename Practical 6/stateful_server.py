from xmlrpc.server import SimpleXMLRPCServer


class StatefulCounter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count


server = SimpleXMLRPCServer(("127.0.0.1", 8001), allow_none=True)
server.register_instance(StatefulCounter())
print("Stateful server running on port 8001")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nStateful server stopped")
    server.server_close()
