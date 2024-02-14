import subprocess
import json
import psutil


def system_stats():
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

    # Getting memory usage
    memory = psutil.virtual_memory()
    memory_info = {
        "Total": memory.total,
        "Available": memory.available,
        "Used": memory.used,
        "Free": memory.free,
        "Percentage": memory.percent
    }


    # Getting disk usage (used and free)
    try:
        disk_usage_output = subprocess.check_output(["df", "-h"]).decode()
        disk_usage_info = disk_usage_output.strip().split("\n")[1:]
        disk_info = {}
        for line in disk_usage_info:
            parts = line.split()
            if len(parts) >= 6 and parts[5] == '/':
                disk_used = parts[2]
                disk_available = parts[3]
                disk_total = parts[1]
                disk_percentage = parts[4]



    except subprocess.CalledProcessError:
        disk_info = {"Error": "Unable to fetch disk usage information"}


    # Getting uptime, load average, and number of tasks running
    uptime = subprocess.check_output(["uptime", "-p"]).decode().strip()
    load_average = subprocess.check_output(["uptime"]).decode().strip().split()[-3:]
    load_average_cleaned = [value.rstrip(",") for value in load_average]



    # Getting CPU information
    cpu_info = {
        "Cores": psutil.cpu_count(logical=True),
        "Total Percentage": psutil.cpu_percent(),
        "Per Core Percentage": psutil.cpu_percent(percpu=True)
    }

    # Getting CPU temperature
    def get_cpu_temperature():
        try:
            with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
                temperature_str = f.read().strip()
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
        #  "Voltage Information": {
        #     # "Operating Voltage": voltage
        # },
        "Disk Usage": {
            "Used": disk_used,
            "Available": disk_available,
            "Total": disk_total,
            "Percentage": disk_percentage,

    },
        "System Status": {
            "Uptime": uptime,
            "Load Average": load_average_cleaned,
            "Temperature": get_cpu_temperature()  # Adding temperature information
        },
        "Memory Information": memory_info,
        "CPU Information": cpu_info,
    }

    # Convert the dictionary to a JSON string
    json_data = json.dumps(info_dict, indent=4)

    # Print the JSON string
    print(json_data)
    return json_data