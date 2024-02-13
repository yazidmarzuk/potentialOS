import subprocess
import json
# import constants

# Getting system information
Architecture = subprocess.check_output(["uname", "-m"]).decode().strip()
Machine = "Jetson Xavier"  # Assuming the script is running on a Jetson Xavier
Node = subprocess.check_output(["uname", "-n"]).decode().strip()
System = "Linux"  # Assuming it's a Linux system

# Getting connected network interface and SSID
try:
    iw_output = subprocess.check_output(["iw", "dev"]).decode()
    network_interface = iw_output.split("Interface ")[1].split("\n")[0]
    ssid_output = subprocess.check_output(["iw", "dev", network_interface, "link"]).decode()
    ssid = ssid_output.split("SSID: ")[1].split("\n")[0]
except subprocess.CalledProcessError:
    network_interface = "Unknown"
    ssid = "Unknown"

# Getting operating voltage (Assuming Jetson Xavier)
# voltage = subprocess.check_output(["sudo", "nvpmodel", "-q"]).decode().strip().split('\n')[0]

# Getting disk usage (used and free)
try:
    disk_usage_output = subprocess.check_output(["df", "-h"]).decode()
    disk_usage_info = disk_usage_output.strip().split("\n")[1:]
    disk_info = {}
    for line in disk_usage_info:
        parts = line.split()
        if len(parts) >= 6 and parts[5] == '/':
            disk_info["Used"] = parts[2]
            disk_info["Available"] = parts[3]
            disk_info["Total"] = parts[1]
except subprocess.CalledProcessError:
    disk_info = {"Error": "Unable to fetch disk usage information"}

# Getting uptime, load average, and number of tasks running
uptime = subprocess.check_output(["uptime", "-p"]).decode().strip()
load_average = subprocess.check_output(["uptime"]).decode().strip().split()[-3:]

# Getting system temperature
def get_system_temperature():
    try:
        # Read the temperature from the thermal zone file
        with open("/sys/devices/virtual/thermal/thermal_zone0/temp", "r") as f:
            temperature_str = f.read().strip()

        # Convert the temperature from millidegrees Celsius to degrees Celsius
        temperature_celsius = int(temperature_str) / 1000

        return temperature_celsius
    except Exception as e:
        return f"Error: {e}"

# Creating a dictionary with the collected information
info_dict = {
    "System Information": {
        "Architecture": Architecture,
        "Machine": Machine,
        "Node": Node,
        "System": System
    },
    "Network Information": {
        "Connected Network Interface": network_interface,
        "SSID": ssid
    },
    "Voltage Information": {
        # "Operating Voltage": voltage
    },
    "Disk Usage": {
        "nvme0n1p1": disk_info
    },
    "System Status": {
        "Uptime": uptime,
        "Load Average": load_average,
        "Temperature": get_system_temperature()  # Adding temperature information
    }
}

# Convert the dictionary to a JSON string
json_data = json.dumps(info_dict, indent=4)

# Print the JSON string
print(json_data)