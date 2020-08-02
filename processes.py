import os
import wmi
import getpass

def checkproc(ip_addr):
	username = input('Username: ')
	passwordw = getpass.getpass('Password: ')
	
	conn = wmi.WMI(ip_addr, user=username, password=passwordw)
	for process in conn.Win32_Process():
		print("ID: {0}\nHandleCount: {1}\nProcessName: {2}\n".format(
		    process.ProcessId, process.HandleCount, process.Name
		    )
		)