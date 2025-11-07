import pandas as pd

def load_logs(file_path='sample_logs/system_logs.csv'):
    df = pd.read_csv(file_path, parse_dates=['timestamp'])
    return df

def tail_logs(file_path='sample_logs/system_logs.csv', n=10):
    df = pd.read_csv(file_path, parse_dates=['timestamp'])
    return df.tail(n)
