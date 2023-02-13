import re
from netmiko import ConnectHandler

def get_int_brief(device_params):
    with ConnectHandler(**device_params) as ssh:
        int_brief = ssh.send_command('show ip int br')
        return int_brief

def get_route(device_params):
    with ConnectHandler(**device_params) as ssh:
        manage_route = ssh.send_command(f'show ip route vrf management \
            | include ^C').strip().split('\n')[1:]
        data_route = ssh.send_command(f'show ip route vrf control-data \
            | include ^C').strip().split('\n')[1:]
        return "\n".join(manage_route + data_route)

def get_int_des(device_params, int_name):
    with ConnectHandler(**device_params) as ssh:
        int_des = ssh.send_command('show int des')
        return int_des

def get_ip(device_params, int_name):
    data = get_int_brief(device_params)
    result = data.strip().split('\n')
    for line in result[1:]:
        int_type, int_num, int_ip = re.search('(\w)\w+(\d+/\d+)\s+(\d+\.\d+\.\d+\.\d+|unassigned).*', line).groups()
        if int_type == int_name[0] and int_num == int_name[1:]:
            return int_ip

def get_netmask(device_params, int_name):
    route = get_route(device_params)
    result = route.strip().split('\n')
    for line in result:
        netmask, int_type, int_num = re.search('.+/(\d+).+\, (\w)\D+(\d/\d)', line).groups()
        if int_type == int_name[0] and int_num == int_name[1:]:
            return netmask
        

def get_des(device_params, int_name):
    int_des = get_int_des(device_params, int_name)
    result = int_des.strip().split('\n')
    for line in result[1:]:
        int_type, int_num, desc = re.search('(\w)\D(\d/\d).+(N.+|C.+)', line).groups()
        if int_type == int_name[0] and int_num == int_name[1:]:
            return desc
def get_status(device_params, int_name):
    int_des = get_int_des(device_params, int_name)
    result = int_des.strip().split('\n')
    for line in result[1:]:
        int_type, int_num, status, proto = re.search('(\w)\D(\d/\d)\s+(\w+ down|\w+)\s+(up|down)', line).groups()
        if int_type == int_name[0] and int_num == int_name[1:]:
            return f'{status}/{proto}'
if __name__ == '__main__':
    device_ip = '172.31.102.4'
    username = 'admin'
    pri_key = '/home/devasc/.ssh/id_rsa'

    device_params = {
        'device_type': 'cisco_ios',
        'ip': device_ip,
        'username': username,
        'use_keys': True,
        'key_file': pri_key
        }
    print(get_ip(device_params, 'G0/0'))
    print(get_netmask(device_params, 'G0/0'))
    print(get_des(device_params, 'G0/0'))
    print(get_status(device_params, 'G0/0'))
