from netmiko import ConnectHandler

def get_int_info_brief(device_params):
    with ConnectHandler(**device_params) as ssh:
        ints_info = ssh.send_command('show ip int br')
        return ints_info

def get_ip(device_params, int_name):
    data = get_int_info_brief(device_params)
    result = data.strip().split('\n')
    for line in result[1:]:
        words = line.split()
        if words[0][0] == int_name[0] and words[0][-3:] == int_name[1:]:
            return words[1]

def get_int_info(device_params, int_name):
    with ConnectHandler(**device_params) as ssh:
        int_info = ssh.send_command(f'show int {int_name}')
        return int_info

def get_netmask(device_params, int_name):
    int_info = get_int_info(device_params, int_name)
    lines = int_info.strip().split('\n')
    netmask = lines[2].split('/')[1]
    return netmask

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
    