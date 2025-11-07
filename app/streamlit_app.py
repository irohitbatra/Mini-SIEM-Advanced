import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
from src.ingest import load_logs, tail_logs
from src.auth_detection import detect_brute_force, detect_impossible_travel
from src.file_monitor import detect_suspicious_files, detect_log_deletion
from src.network_analysis import detect_port_scanning, detect_repeated_connections
from src.malware_detection import detect_malware, detect_suspicious_processes
from src.correlator import load_rules, correlate
from src.alerts import generate_alerts
from src.utils import summarize_logs
import plotly.express as px

st.set_page_config(page_title="Mini-SIEM Advanced Dashboard", layout="wide")
st.title("Mini-SIEM Advanced Dashboard 🚨")

# Load logs
logs = load_logs()
st.subheader("Latest Logs")
st.dataframe(tail_logs(n=20))

# Authentication attack detection
st.subheader("Authentication Attacks")
brute_force = detect_brute_force(logs)
impossible_travel = detect_impossible_travel(logs)
st.write("Brute Force Attempts")
st.dataframe(brute_force)
st.write("Impossible Travel Detected")
st.dataframe(impossible_travel)

# File/System monitoring
st.subheader("File/System Monitoring")
suspicious_files = detect_suspicious_files(logs)
log_deletion = detect_log_deletion(logs)
st.write("Suspicious Executable Files Created")
st.dataframe(suspicious_files)
st.write("Deleted Logs / Tampering")
st.dataframe(log_deletion)

# Network analysis
st.subheader("Network Analysis")
port_scan = detect_port_scanning(logs)
repeated_conn = detect_repeated_connections(logs)
st.write("Port Scanning Detected")
st.dataframe(port_scan)
st.write("Repeated Connection Attempts")
st.dataframe(repeated_conn)

# Malware indicators
st.subheader("Malware Indicators")
malware = detect_malware(logs)
suspicious_proc = detect_suspicious_processes(logs)
st.write("Malicious Hashes Detected")
st.dataframe(malware)
st.write("Suspicious Processes")
st.dataframe(suspicious_proc)

# Rule-based alerting
st.subheader("Correlated Alerts")
rules = load_rules()
alerts = correlate(logs, rules)
st.text(generate_alerts(alerts))

# Summary plots
st.subheader("Log Summary")
summary = summarize_logs(logs)
if not summary.empty:
    fig = px.bar(summary, x='event', y='count', color='level', barmode='group', title="Event Counts by Level")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No log data available for summary.")
