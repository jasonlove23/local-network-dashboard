import subprocess
import platform

def ping_device(ip):
    """
    Pings a device and returns True if online, False if offline
    """
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", ip]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0
