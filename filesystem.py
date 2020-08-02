import os
import wmi
import getpass
import colorama

def checkfs(ip_addr, target_user):
    colorama.init(autoreset=True)
    paths = [
        '\\\\' + ip_addr + '\\c$\\users\\' + target_user + '\\',
        '\\\\' + ip_addr + '\\c$\\users\\' + target_user + '\\appdata\\local',
        '\\\\' + ip_addr + '\\c$\\users\\' + target_user + '\\appdata\\roaming'
        ]
    
    #files_user = [f for f in os.listdir(paths[0]) if os.path.isfile(paths[0] + "\\" + f)]
    files_local = [f for f in os.listdir(paths[1]) if os.path.isfile(paths[1] + "\\" + f)]
    files_roaming = [f for f in os.listdir(paths[2]) if os.path.isfile(paths[2] + "\\" + f)]
    files_user = [f for f in os.listdir(paths[0])]

    print("User:\n[+] Discovered:")
    for file in files_user:
        if os.path.isfile(paths[0] + "\\" + file):
            print(" - " + file)
        else:
            print(colorama.Fore.RED + " - " + file)
    
    print("Local:\n[+] Discovered:")
    for file in files_local:
        print(" - " + file)
    
    print("Roaming:\n[+] Discovered:")
    for file in files_roaming:
        print(" - " + file)


# Function to get all local users.
def getusers(ip):
    path = '\\\\' + ip + '\\c$\\users\\'
    users = [f for f in os.listdir(path) if os.path.isdir(path + "\\" + f)]

    # remove invalid users.
    invalidUsers = [
        "All Users",
        "Default",
        "Default User",
    ]

    for user in invalidUsers:
        if user in users:
            users.remove(user)
    
    return users