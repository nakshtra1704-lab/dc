"""Start a local concurrent echo server and interactive client together."""

import argparse
import threading

from echo_client import run_client
from echo_server import create_server


def main():
    parser = argparse.ArgumentParser(
        description="Run a local concurrent echo server and client."
    )
    parser.add_argument("port", nargs="?", type=int, default=5000)
    arguments = parser.parse_args()

    try:
        server = create_server(arguments.port)
    except OSError as error:
        print(f"Could not start the server on port {arguments.port}: {error}")
        return 1

    server_thread = threading.Thread(target=server.serve_forever, daemon=True)
    server_thread.start()
    print(f"Local concurrent echo server started on port {arguments.port}")

    try:
        return run_client("localhost", arguments.port)
    finally:
        server.shutdown()
        server.server_close()
        server_thread.join()
        print("Local server stopped.")


if __name__ == "__main__":
    raise SystemExit(main())
