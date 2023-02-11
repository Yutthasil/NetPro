from netmiko import *
from netmikolab01 import get_ip
from netmikolab01 import get_netmask

devices_ip = ['172.31.102.4', '172.31.102.5', '172.31.102.6']
username = 'admin'
pri_key = '/home/devasc/.ssh/id_rsa'

device_params1 = {
    'device_type': 'cisco_ios',
    'ip': devices_ip[0],
    'username': username,
    'use_keys': True,
    'key_file': pri_key
    }
device_params2 = {
    'device_type': 'cisco_ios',
    'ip': devices_ip[1],
    'username': username,
    'use_keys': True,
    'key_file': pri_key
    }
device_params3 = {
    'device_type': 'cisco_ios',
    'ip': devices_ip[2],
    'username': username,
    'use_keys': True,
    'key_file': pri_key
    }

def test_ip():
    assert get_ip(device_params1, 'G0/0') == '172.31.102.4'
    assert get_netmask(device_params1, 'G0/0') == '28'
    assert get_ip(device_params1, 'G0/1') == '172.31.102.17'
    assert get_netmask(device_params1, 'G0/1') == '28'
    assert get_ip(device_params1, 'G0/2') == '172.31.102.34'
    assert get_netmask(device_params1, 'G0/2') == '28'
    assert get_ip(device_params1, 'G0/3') == 'unassigned'

    assert get_ip(device_params2, 'G0/0') == '172.31.102.5'
    assert get_netmask(device_params2, 'G0/0') == '28'
    assert get_ip(device_params2, 'G0/1') == '172.31.102.33'
    assert get_netmask(device_params2, 'G0/1') == '28'
    assert get_ip(device_params2, 'G0/2') == '172.31.102.50'
    assert get_netmask(device_params2, 'G0/2') == '28'
    assert get_ip(device_params2, 'G0/3') == 'unassigned'