import xmlrpc.client


server = xmlrpc.client.ServerProxy("http://127.0.0.1:8002/")
value = 0

for request_number in range(1, 4):
    value = server.increment(value)
    print(f"Request {request_number}: client value = {value}")
