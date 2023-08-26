import socket

hostname = socket.gethostname()
ip_addr = socket.gethostbyname(hostname)
ip_addr = f"{ip_addr}:443"
print(ip_addr)
print(f"Your ip is {ip_addr.split(':')[0]} and you port is {ip_addr.split(':')[1]}")