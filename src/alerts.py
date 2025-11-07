import json

def generate_alerts(alerts):
    if not alerts:
        return "No alerts triggered."
    output = ""
    for alert in alerts:
        output += f"ALERT {alert['rule_id']} ({alert['level']}): {alert['description']} - Matches: {alert['matches']}\n"
    return output

def export_alerts_json(alerts, file_path='alerts.json'):
    with open(file_path, 'w') as f:
        json.dump(alerts, f, indent=4)
