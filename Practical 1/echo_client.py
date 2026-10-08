import argparse
import socket     
def run_client(host, port):
    """Connect to an echo server and exchange interactive messages."""
    try:
        with socket.create_connection((host, port)) as connection:
            with connection.makefile("rwb") as stream:
                print(f"Connected to {host}:{port}")
                print("Type a message and press Enter. Type 'exit' to close.")

                while True:
                    message = input("> ")
                    stream.write(f"{message}\n".encode("utf-8"))
                    stream.flush()

                    echo = stream.readline()
                    if not echo:
                        print("Server closed the connection.")
                        return 1

                    print(f"Echo from server: {echo.decode('utf-8').rstrip()}")
                    if message.strip().lower() == "exit":
                        return 0
    except ConnectionRefusedError:
        print(f"Connection refused: no server is running on {host}:{port}.")
        print(f"Run 'python echo_server.py {port}' in another terminal first.")
        print("Or run 'python run_echo.py' to start both automatically.")
        return 1
    except OSError as error:
        print(f"Client error: {error}")
        return 1
    except (EOFError, KeyboardInterrupt):
        print("\nClient stopped.")
        return 0


def main():
    parser = argparse.ArgumentParser(description="Connect to a TCP echo server.")
    parser.add_argument("host", nargs="?", default="localhost")
    parser.add_argument("port", nargs="?", type=int, default=5000)
    arguments = parser.parse_args()

    return run_client(arguments.host, arguments.port)


if __name__ == "__main__":
    raise SystemExit(main())
