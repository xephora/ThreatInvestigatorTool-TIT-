import os
import wmi
import getpass

def checkfs(ip_addr):
    target_user = input('Target Username?: ')
    paths = [
        '\\\\' + ip_addr + '\\c$\\users\\' + target_user + '\\',
        '\\\\' + ip_addr + '\\c$\\users\\' + target_user + '\\appdata\\local',
        '\\\\' + ip_addr + '\\c$\\users\\' + target_user + '\\appdata\\roaming'
        ]
    
    files_users = [f for f in os.listdir(paths[0]) if os.path.isfile(paths[0] + "\\" + f)]
    files_local = [f for f in os.listdir(paths[1]) if os.path.isfile(paths[1] + "\\" + f)]
    files_roaming = [f for f in os.listdir(paths[2]) if os.path.isfile(paths[2] + "\\" + f)]

    print("User:\n[+] Discovered:")
    for file in files_users:
        print(" - " + file)
    
    print("Local:\n[+] Discovered:")
    for file in files_local:
        print(" - " + file)
    
    print("Roaming:\n[+] Discovered:")
    for file in files_roaming:
        print(" - " + file)