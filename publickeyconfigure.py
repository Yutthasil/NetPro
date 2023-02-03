import pexpect

PROMPT = '#'
IPs = ['172.31.102.1', '172.31.102.2', '172.31.102.3', '172.31.102.4', '172.31.102.5', '172.31.102.6']
USERNAME = 'admin'   
PASSWORD = 'cisco'

for ip in IPs:
    child = pexpect.spawn('telnet ' + ip)
    child.expect('Username')
    child.sendline(USERNAME)
    child.expect('Password')
    child.sendline(PASSWORD)
    child.expect(PROMPT)
    child.sendline('configure terminal')
    child.expect(PROMPT)
    child.sendline('ip ssh pubkey-chain')
    child.expect(PROMPT)
    child.sendline('username admin')
    child.expect(PROMPT)
    child.sendline('key-string')
    child.expect(PROMPT)
    child.sendline('AAAAB3NzaC1yc2EAAAADAQABAAABAQDP0gOeMIL8YEur7A+ZsW0LXTwHgYlv8t88')
    child.expect(PROMPT)
    child.sendline('NuZBTfXmpIeGJExwqz4d/j/XP2khdNAf6eHNcXe+036/vHA23Xq7NWHcxmxEdWJ7eBCtiICU')
    child.expect(PROMPT)
    child.sendline('55MdmdjEf8SG6/bw6wWCiN1qk0YWneFD2a/J6mumIgyGm12NBJGuSbqnpSryFC8/czL04rQ3')
    child.expect(PROMPT)
    child.sendline('dwh8oSt1ngott7F16JT+Jn2UWePGLcmyyHa0MIZcIF89B7xVW7nlfKU4t0Y+kMbm0//n3RjM')
    child.expect(PROMPT)
    child.sendline('E8eDWu2eidP0iyLOroNNUHufdno0bg5gLz+vdfEsT3LmxKh4NAj1biNjM1FJn4cAI2LXbUcA')
    child.expect(PROMPT)
    child.sendline('sAdYEcuISPabjKjxwdv5')
    child.expect(PROMPT)
    child.sendline('exit')
    child.expect(PROMPT)
    child.sendline('no ip ssh server authenticate user password')
    child.expect(PROMPT)
    child.sendline('no ip ssh server authenticate user keyboard')
    child.expect(PROMPT)
    child.sendline('exit')
    print(f'configure ssh on {ip} completed.')
print("All done!!!")
