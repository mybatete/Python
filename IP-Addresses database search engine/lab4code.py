
from ListNode import Node
from lab4class import IPAddress

fp = open ("Residence_Hall_IPs.dat","r")

temp = Node()

while True:
    line = fp.readline()
    if line == "":
        break
    line = line.strip()
    n = line. split()
    ip = n[0]
    t = IPAddress(ip, 1)
    temp.add(t)
print ip
print temp.traversal()
