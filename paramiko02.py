import time
import paramiko

username = 'admin'

devices_ip = ['172.31.102.1', '172.31.102.2', '172.31.102.3', \
'172.31.102.4', '172.31.102.5', '172.31.102.6']

for ip in devices_ip:
    client = paramiko.SSHClient()
    # accept fingerprint.
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # looking private key for public key authentication.
    client.connect(hostname=ip, username=username, look_for_keys=True) 
    print("Connecting to {} ...".format(ip))
    with client.invoke_shell() as ssh:
        print("Connected to {} ...".format(ip))

        ssh.send("terminal length 0\n")
        time.sleep(1)
        result = ssh.recv(1000).decode('ascii')
        print(result)

        ssh.send("sh ip int br\n")
        time.sleep(1)
        result = ssh.recv(1000).decode('ascii')
        print(result)