import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Automatically add the server's SSH key (not recommended for production code)

private_key_path = r"C:\Users\tiger\.ssh\id_rsa"
mykey = paramiko.RSAKey(filename=private_key_path)
username = "root"
ip_address = "38.147.83.13"
port = 44301

ssh.connect(ip_address, port=port, username=username, pkey=mykey)

stdin, stdout, stderr = ssh.exec_command('ls')  # Replace 'ls' with your command
print(stdout.read().decode())
print(stderr.read().decode())

ssh.close()