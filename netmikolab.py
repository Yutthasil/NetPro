from netmiko import ConnectHandler


def get_int_brief(device_params):
    with ConnectHandler(**device_params) as ssh:
        int_brief = ssh.send_command('show ip int br', use_textfsm=True)
        return int_brief

def get_route(device_params):
    with ConnectHandler(**device_params) as ssh:
        manage_route = ssh.send_command(f'show ip route vrf management', use_textfsm=True)
        data_route = ssh.send_command(f'show ip route vrf control-data', use_textfsm=True)
        return manage_route + data_route

def get_int_des(device_params, int_name):
    with ConnectHandler(**device_params) as ssh:
        int_des = ssh.send_command('show int des', use_textfsm=True)
        return int_des

def get_ip(device_params, int_name):
    data = get_int_brief(device_params)
    for intf in data:
        if intf['intf'][0] == int_name[0] \
        and intf['intf'][-3:] == int_name[1:]:
            return intf['ipaddr']

def get_netmask(device_params, int_name):
    routes = get_route(device_params)
    for route in routes:
        if route['protocol'] == 'C' \
        and route['nexthop_if'][0] == int_name[0]\
        and route['nexthop_if'][-3:] == int_name[1:]:
            return route['mask']
        
def get_des(device_params, int_name):
    ints_des = get_int_des(device_params, int_name)
    for des in ints_des:
        if des['port'][0] + des['port'][2:] == int_name:
            return des['descrip']

def get_status(device_params, int_name):
    ints_des = get_int_des(device_params, int_name)
    for des in ints_des:
        if des['port'][0] + des['port'][2:] == int_name:
            return f"{des['status']}/{des['protocol']}"

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
    #print(get_ip(device_params, 'G0/0'))
    #print(get_netmask(device_params, 'G0/2'))
    #print(get_des(device_params, 'G0/3'))
    print(get_status(device_params, 'G0/3'))
