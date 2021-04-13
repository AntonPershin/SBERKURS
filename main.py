import socket
sock = socket.socket()
print("Enter deal ID:")
inputID = int(input())

print("Enter date:")
inputDate = input()
print("---------")
inputDate = input()
sock.connect('localhost',9090)
istr = inputID +" "+ inputDate
print (istr.split()[1])
sock.send(istr.encode("utf8"))
data = sock.recv(1024)
sock.close()
print(data.decode("utf8"))