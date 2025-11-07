import pandas as pd
import random
from datetime import datetime, timedelta

users = ['root', 'admin', 'guest', 'service']
events = ['login', 'logout', 'file_change', 'file_delete', 'process_start', 'network_connect']
countries = ['India', 'USA', 'UK', 'Germany', 'China']
levels = ['INFO', 'WARNING', 'ERROR', 'CRITICAL']

def generate_logs(num=1000):
    logs = []
    start_time = datetime.now() - timedelta(days=1)
    for _ in range(num):
        timestamp = start_time + timedelta(seconds=random.randint(0, 86400))
        log = {
            'timestamp': timestamp,
            'user': random.choice(users),
            'event': random.choice(events),
            'level': random.choice(levels),
            'country': random.choice(countries),
            'file': f"/tmp/{random.choice(['test.txt','malware.exe','data.log','config.cfg'])}",
            'process': random.choice(['cmd.exe','powershell.exe','notepad.exe','malicious.exe']),
            'hash': random.choice(['abcd1234','efgh5678','ijkl9012','malwarehash']),
            'description': 'Sample log event'
        }
        logs.append(log)
    df = pd.DataFrame(logs)
    df.to_csv('sample_logs/system_logs.csv', index=False)
    print("Sample logs generated at sample_logs/system_logs.csv")

if __name__ == "__main__":
    generate_logs()
