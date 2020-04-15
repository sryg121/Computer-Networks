import httplib

host = '127.0.0.1'
port = 9090
conn = httplib.HTTPConnection(host,port)

# request 'index.html'
conn.request("GET", "./index.html")
response = conn.getresponse()

# request 'image.jpg'
conn.request("GET", "./image.jpg")
respose = conn.getresponse()

data1 = response.read()
print data1