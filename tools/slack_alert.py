# tools/slack_alert.py
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--message", type=str, required=True)
args = parser.parse_args()

webhook = "https://hooks.slack.com/services/YOUR/HOOK"
payload = {"text": f"AI ALERT: {args.message}"}
requests.post(webhook, json=payload)
print("Slack alert sent")
