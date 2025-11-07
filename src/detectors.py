import pandas as pd
import numpy as np

def detect_anomalies(df, column="level"):
    # Convert level to numeric score
    level_map = {"INFO": 1, "WARNING": 2, "ERROR": 3, "CRITICAL": 4}
    df['level_score'] = df[column].map(level_map)
    
    mean = df['level_score'].mean()
    std = df['level_score'].std()
    
    df['anomaly'] = np.abs(df['level_score'] - mean) > 2 * std
    return df[df['anomaly']]
