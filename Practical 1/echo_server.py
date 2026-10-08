"""Concurrent TCP echo server."""

import argparse
import socketserver


class EchoRequestHandler(socketserver.StreamRequestHandler):
    """Echo each newline-delimited message from one client."""

    def handle(self):
        client_address = f"{self.client_address[0]}:{self.client_address[1]}"
        print(f"Client connected: {client_address}")

        for message in self.rfile:
            self.wfile.write(message)
            self.wfile.flush()

            if message.decode("utf-8").strip().lower() == "exit":
                break

        print(f"Client disconnected: {client_address}")


class ConcurrentEchoServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


def create_server(port):
    """Create a concurrent echo server listening on the given port."""
    return ConcurrentEchoServer(("", port), EchoRequestHandler)


def main():
    parser = argparse.ArgumentParser(description="Run a concurrent TCP echo server.")
    parser.add_argument("port", nargs="?", type=int, default=5000)
    arguments = parser.parse_args()

    with create_server(arguments.port) as server:
        print(f"Concurrent echo server started on port {arguments.port}")
        print("Press Ctrl+C to stop the server.")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")


if __name__ == "__main__":
    main()
