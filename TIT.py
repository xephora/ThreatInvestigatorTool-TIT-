import filesystem, registry, processes, getpass


# Function to ensure the user enters a valid ip.
def get_valid_ip():
    while True:
        ip = input("Enter an ip: ")
        try:
            octets = ip.split(".")
            if len(octets) != 4:
                print("[!] Invalid ip...")
                continue

            for octet in octets:
                if int(octet) > 255 or int(octet) < 0:
                    print("[!] Invalid ip...")
                    continue
            break
        except:
            continue
    return ip


# If this file is being ran directly, not imported.
if __name__ == "__main__":
    ip = get_valid_ip()
    users = filesystem.getUsers()
    username = select_user()
    password = getpass.getpass("Password: ")

    
    