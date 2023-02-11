from netmiko import ConnectHandler

def get_int_brief(device_params):
    with ConnectHandler(**device_params) as ssh:
        int_brief = ssh.send_command('show ip int br')
        return int_brief

def get_route(device_params):
    with ConnectHandler(**device_params) as ssh:
        manage_route = ssh.send_command(f'show ip route vrf management | include ^C')
        data_route = ssh.send_command(f'show ip route vrf control-data | include ^C')
        return manage_route + "\n" + data_route

def get_int_des(device_params, int_name):
    with ConnectHandler(**device_params) as ssh:
        int_des = ssh.send_command('show int des')
        return int_des

def get_ip(device_params, int_name):
    data = get_int_brief(device_params)
    result = data.strip().split('\n')
    for line in result[1:]:
        words = line.split()
        if words[0][0] == int_name[0] and words[0][-3:] == int_name[1:]:
            return words[1]

def get_netmask(device_params, int_name):
    route = get_route(device_params)
    result = route.strip().split('\n')
    for line in result[1:]:
        words = line.split()
        if words[0] == 'C' and words[-1][0] == int_name[0] and words[-1][-3:] == int_name[1:]:
            netmask = words[1].split('/')[1]
            return netmask

def get_des(device_params, int_name):
    int_des = get_int_des(device_params, int_name)
    result = int_des.strip().split('\n')
    for line in result[1:]:
        words = line.split()
        if words[0][0] == int_name[0] and words[0][2:] == int_name[1:]:
            if words[1] != 'admin':
                return " ".join(words[3:])
            return " ".join(words[4:])

def get_status(device_params, int_name):
    int_des = get_int_des(device_params, int_name)
    result = int_des.strip().split('\n')
    for line in result[1:]:
        words = line.split()
        if words[0][0] == int_name[0] and words[0][2:] == int_name[1:]:
            if words[1] != 'admin':
                return f'{words[1]}/{words[2]}'
            return f'{words[1]} {words[2]}/{words[3]}'
    
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
