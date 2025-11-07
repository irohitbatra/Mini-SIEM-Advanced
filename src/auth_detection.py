import pandas as pd
from datetime import timedelta

def detect_brute_force(df):
    df_login = df[df['event']=='login']
    df_grouped = df_login.groupby('user').size().reset_index(name='attempts')
    return df_grouped[df_grouped['attempts']>5]

def detect_impossible_travel(df):
    df_login = df[df['event']=='login'].sort_values('timestamp')
    alerts = []
    users = df_login['user'].unique()
    for user in users:
        user_logs = df_login[df_login['user']==user]
        user_logs = user_logs.reset_index()
        for i in range(1, len(user_logs)):
            t1 = user_logs.loc[i-1, 'timestamp']
            c1 = user_logs.loc[i-1, 'country']
            t2 = user_logs.loc[i, 'timestamp']
            c2 = user_logs.loc[i, 'country']
            diff = (t2 - t1).total_seconds() / 60
            if diff < 120 and c1 != c2:
                alerts.append({
                    'user': user,
                    'from_country': c1,
                    'to_country': c2,
                    'timestamp': t2,
                    'description': 'Impossible travel detected'
                })
    return pd.DataFrame(alerts)
