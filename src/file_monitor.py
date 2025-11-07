def detect_suspicious_files(df):
    suspicious = df[df['file'].str.endswith('.exe')]
    return suspicious

def detect_log_deletion(df):
    deletion_logs = df[df['event']=='file_delete']
    return deletion_logs
