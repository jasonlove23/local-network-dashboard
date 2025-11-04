import streamlit as st
import pandas as pd
import os
from scanner import ping_device
from logger import log_device_status

devices = {
    "Router": "192.168.1.1",
    "Laptop": "192.168.1.10",
    "Phone": "192.168.1.15"
}

st.set_page_config(page_title="Local Security & Network Visibility", layout="wide")
st.title("🔒 Local Security & Network Visibility Tool")

if st.button("Run Scan"):
    results = []
    for device, ip in devices.items():
        status = "Online" if ping_device(ip) else "Offline"
        log_device_status(device, ip, status)
        results.append({"Device": device, "IP": ip, "Status": status})

    df = pd.DataFrame(results)
    df["Status"] = df["Status"].apply(lambda x: "🟢 Online" if x == "Online" else "🔴 Offline")
    st.dataframe(df, use_container_width=True)

if os.path.exists("data/device_log.csv"):
    st.subheader("📜 Log History")
    log_data = pd.read_csv("data/device_log.csv", header=None, names=["Time", "Device", "IP", "Status"])
    st.dataframe(log_data.tail(10), use_container_width=True)
