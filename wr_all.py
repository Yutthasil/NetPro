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
    child.sendline('configure terminal')
    child.expect(PROMPT)
    child.sendline('wr')
    child.expect(PROMPT)
    print(f"{ip}'s configuration has been saved!!")
print("All done!")