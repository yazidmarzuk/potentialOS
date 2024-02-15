import psutil
import json
from datetime import datetime

def get_processes():
    processes = []
    for proc in psutil.process_iter(['pid', 'username', 'cpu_percent', 'memory_percent', 'create_time', 'cmdline']):
        try:
            processes.append({
                'pid': proc.info['pid'],
                'username': proc.info['username'],
                'cpu_percent': proc.info['cpu_percent'],
                'memory_percent': proc.info['memory_percent'],
                'start_time': datetime.fromtimestamp(proc.info['create_time']).strftime('%Y-%m-%d %H:%M:%S'),
                'command': ' '.join(proc.info['cmdline']) if proc.info['cmdline'] else ''
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return json.dumps(processes)