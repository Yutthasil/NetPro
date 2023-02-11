from netmiko import ConnectHandler

device_ip = input("Insert Device IP address: ")
username = 'admin'
pri_key = '/home/devasc/.ssh/id_rsa'

device_params = {
    'device_type': 'cisco_ios',
    'ip': device_ip,
    'username': username,
    'use_keys': True,
    'key_file': pri_key
}

with ConnectHandler(**device_params) as ssh:
    result = ssh.send_command('show ip int br')
    print(result)
    result = ssh.send_command('show cdp neighbors')
    print(result)
    result = ssh.send_command('show int description')
    print(result)
    result = ssh.send_command('show ip route vrf management | include ^C')
    print(result)
    result = ssh.send_command('show ip route vrf control-data | include ^C')
    print(result)

