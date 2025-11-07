import yaml

def load_rules(file_path='rules/rules.yaml'):
    with open(file_path) as f:
        rules = yaml.safe_load(f)
    return rules['rules']

def correlate(df, rules):
    alerts = []
    for rule in rules:
        matched = df[df['event']==rule['event']]
        if len(matched) >= rule['threshold']:
            alerts.append({
                'rule_id': rule['id'],
                'description': rule['description'],
                'matches': len(matched),
                'level': rule['level']
            })
    return alerts
