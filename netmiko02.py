from netmiko import ConnectHandler
from jinja2 import Template
import yaml

devices_ip = ['172.31.102.4', '172.31.102.5', '172.31.102.6']
username = 'admin'
pri_key = 'id_rsa'
# pri_key = '/home/devasc/.ssh/id_rsa'


#prepare jinja2 template
template = open("config/intf_des_template.txt", "r")
template = template.read()

#loop to config each Router
for device_ip in devices_ip:
    device_params = {
            'device_type': 'cisco_ios',
            'ip': device_ip,
            'username': username,
            'use_keys': True,
            'key_file': pri_key
            }
    
    #open config file
    with open("config/{}.yaml".format(device_ip), "r") as data:
        #parse data in yaml format to dict
        data = yaml.safe_load(data)

        #create jinja2 template object from prepared template
        j2_template = Template(template)
        configs = j2_template.render(data)
    
    with ConnectHandler(**device_params) as ssh:
        result = ssh.send_config_set(configs.split('\n'))
        print(result)
