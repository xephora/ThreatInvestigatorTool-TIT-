import filesystem, registry, processes, getpass, os

# Function to ensure the user enters a valid ip.
def get_valid_ip():
    while True:
        isValid = True
        ip = input("Enter an ip: ")
        try:
            octets = ip.split(".")
            if len(octets) != 4:
                isValid = False

            for octet in octets:
                if int(octet) > 255 or int(octet) < 0:
                    isValid = False
            
            # If this errors out, we cannot access the host for the rest of our enum,
            # therefore the ip is invalid
            os.listdir("\\\\" + ip + "\\c$\\")

            if isValid:
                break
        except:
            isValid = False
    return ip


# Function to ensure the user selects a valid user account.
def select_user(users):
    while True:
        print("Enter the corresponding number to select a user.")
        for i in range(len(users)):
            print("{0}. {1}".format(i + 1, users[i]))
        try:
            selection = int(input(": "))
            user = users[selection - 1]
            break
        except:
            print("You must enter the corresponding number to select a user...")
    return user

# If this file is being ran directly, not imported.
if __name__ == "__main__":
    print("""
   ████████╗██╗████████╗
   ╚══██╔══╝██║╚══██╔══╝
      ██║   ██║   ██║   
      ██║   ██║   ██║   
      ██║   ██║   ██║   
      ╚═╝   ╚═╝   ╚═╝   
(Threat Investigation Tool)
""")
    ip = get_valid_ip()
    users = filesystem.getusers(ip)
    username = select_user(users)
    print("Selected user: {}".format(username))
    password = getpass.getpass("Password: ")

    
    