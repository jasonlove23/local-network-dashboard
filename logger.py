import csv
import os
from datetime import datetime

LOG_FILE = "data/device_log.csv"

def log_device_status(device, ip, status):
    """
    Logs the device status to CSV file
    """
    os.makedirs("data", exist_ok=True)
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), device, ip, status])
