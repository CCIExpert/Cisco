from netmiko import Netmiko
from getpass import getpass

f= open("ips.txt","r")
for IP in f:
    cisco = {
        'host': IP,
        'username': 'admin',
        'password': 'admin',
        'device_type': 'cisco_ios',
        }

    net_connect = Netmiko(**cisco)
    command = 'show ip int brief'

    print()
    print(net_connect.find_prompt())
    output = net_connect.send_command(command)

    print(output)
    print()

    commands = ['router ospf 1',
            'network 0.0.0.0 0.0.0.0 area 0']

    result = net_connect.send_config_set(commands)
    print(result)
    output1=net_connect.send_command("show ip ospf neighbor")
    print(output1)
    output2=net_connect.send_command("show running config ")
    print(output2)

    net_connect.disconnect()
