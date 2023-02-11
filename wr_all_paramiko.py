import time
import paramiko

username = 'admin'

devices_ip = ['172.31.102.1', '172.31.102.2', '172.31.102.3', \
'172.31.102.4', '172.31.102.5', '172.31.102.6']

for ip in devices_ip:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=ip, username=username, look_for_keys=True)
    with client.invoke_shell() as ssh:
        print("Connected to {} ...".format(ip))

        ssh.send("wr\n")
        time.sleep(2)
        ssh.send("exit\n")
        print(f"device {ip}, configuration has been saved.")
print("All devices's configuration has been saved.")