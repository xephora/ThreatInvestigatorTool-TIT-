import os
import wmi
import getpass

# Get all processes.
def check(ip_addr, username):
	passwordw = getpass.getpass('Password: ')
	
	conn = wmi.WMI(ip_addr, user=username, password=passwordw)
	for process in conn.Win32_Process():
		print("ID: {0}\nHandleCount: {1}\nProcessName: {2}\n".format(
		    process.ProcessId, process.HandleCount, process.Name
		    )
		)