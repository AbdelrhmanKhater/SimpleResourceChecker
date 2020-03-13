import http.client
host = input("Type the host: ")
port = int(input("Type the port: "))
resource = input("Type the resource: ")
try:
    connection = http.client.HTTPConnection(host, port)
    connection.request("GET", resource)
    res = connection.getresponse()
    print("Status is ", res.status)
except Exception as e:
    print("Error is", e)
