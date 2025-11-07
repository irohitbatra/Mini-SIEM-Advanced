def summarize_logs(df):
    summary = df.groupby(['level','event']).size().reset_index(name='count')
    return summary
