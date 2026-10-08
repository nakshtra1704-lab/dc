import xmlrpc.client


server = xmlrpc.client.ServerProxy("http://127.0.0.1:8001/")

for request_number in range(1, 4):
    count = server.increment()
    print(f"Request {request_number}: server counter = {count}")
