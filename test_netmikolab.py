from netmiko import *
from netmikolab import *

devices_ip = ['172.31.102.4', '172.31.102.5', '172.31.102.6']
username = 'admin'
pri_key = 'id_rsa'
# pri_key = '/home/devasc/.ssh/id_rsa'

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
    assert get_ip(device_params1, 'G0/1') == '172.31.102.17'
    assert get_ip(device_params1, 'G0/2') == '172.31.102.34'
    assert get_ip(device_params1, 'G0/3') == "unassigned"
    assert get_ip(device_params2, 'G0/0') == '172.31.102.5'
    assert get_ip(device_params2, 'G0/1') == '172.31.102.33'
    assert get_ip(device_params2, 'G0/2') == '172.31.102.50'
    assert get_ip(device_params2, 'G0/3') == "unassigned"
    assert get_ip(device_params3, 'G0/0') == '172.31.102.6'
    assert get_ip(device_params3, 'G0/1') == '172.31.102.49'
    assert get_ip(device_params3, 'G0/3') == "unassigned"

def test_netmask():
    assert get_netmask(device_params1, 'G0/0') == '28'
    assert get_netmask(device_params1, 'G0/1') == '28'
    assert get_netmask(device_params1, 'G0/2') == '28'
    assert get_netmask(device_params2, 'G0/0') == '28'
    assert get_netmask(device_params2, 'G0/1') == '28'
    assert get_netmask(device_params2, 'G0/2') == '28'
    assert get_netmask(device_params3, 'G0/0') == '28'
    assert get_netmask(device_params3, 'G0/1') == '28'
    

def test_description():
    assert get_des(device_params1, 'G0/0') == "Connect to G0/2 of S0"
    assert get_des(device_params1, 'G0/1') == "Connect to G0/2 of S1"
    assert get_des(device_params1, 'G0/2') == "Connect to G0/1 of R2"
    assert get_des(device_params1, 'G0/3') == "Not Use"
    assert get_des(device_params2, 'G0/0') == "Connect to G0/3 of S0"
    assert get_des(device_params2, 'G0/1') == "Connect to G0/2 of R1"
    assert get_des(device_params2, 'G0/2') == "Connect to G0/1 of R3"
    assert get_des(device_params2, 'G0/3') == "Not Use"
    assert get_des(device_params3, 'G0/0') == "Connect to G1/0 of S0"
    assert get_des(device_params3, 'G0/1') == "Connect to G0/2 of R2"
    assert get_des(device_params3, 'G0/2') == "Connect to WAN"
    assert get_des(device_params3, 'G0/3') == "Not Use"

def test_status():
    assert get_status(device_params1, 'G0/0') == 'up/up'
    assert get_status(device_params1, 'G0/1') == 'up/up'
    assert get_status(device_params1, 'G0/2') == 'up/up'
    assert get_status(device_params1, 'G0/3') == 'admin down/down'
    assert get_status(device_params2, 'G0/0') == 'up/up'
    assert get_status(device_params2, 'G0/1') == 'up/up'
    assert get_status(device_params2, 'G0/2') == 'up/up'
    assert get_status(device_params2, 'G0/3') == 'admin down/down'
    assert get_status(device_params3, 'G0/0') == 'up/up'
    assert get_status(device_params3, 'G0/1') == 'up/up'
    assert get_status(device_params3, 'G0/2') == 'up/up'
    assert get_status(device_params3, 'G0/3') == 'admin down/down'