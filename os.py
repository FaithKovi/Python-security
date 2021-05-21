import os
import platform

operating_system = platform.system()
print(operating_system)
if (operating_system == "Windows"):
    ping_command = "ping -n 1 127.0.0.1"
elif (operating_system == "Linux"):
    ping_command = "ping -c 1  127.0.0.1"
else:
    ping_command = "ping -c 1  127.0.0.1"
print(ping_command)

# Display platform processor
print("Platform processor:" , platform.processor())

# Display platform architecture
print("Platform architecture:" , platform.architecture())