from netmiko import ConnectHandler

devices_ip = ['172.31.102.4', '172.31.102.5', '172.31.102.6']
username = 'admin'
pri_key = '/home/devasc/.ssh/id_rsa'

for device_ip in devices_ip:
    device_params = {
            'device_type': 'cisco_ios',
            'ip': device_ip,
            'username': username,
            'use_keys': True,
            'key_file': pri_key
            }
    with ConnectHandler(**device_params) as ssh:
        config_file = f"config/{device_ip}.config" #config/{device_ip}.config
        result = ssh.send_config_from_file(config_file=config_file)
        print(result)

        result = ssh.save_config()
        print(result)