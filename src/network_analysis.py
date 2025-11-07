def detect_port_scanning(df):
    net_logs = df[df['event']=='network_connect']
    counts = net_logs.groupby('user').size().reset_index(name='connections')
    return counts[counts['connections']>10]

def detect_repeated_connections(df):
    net_logs = df[df['event']=='network_connect']
    repeated = net_logs.groupby(['user','file']).size().reset_index(name='count')
    return repeated[repeated['count']>5]
