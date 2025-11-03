# tools/generate_prediction_id.py
import hashlib
import json
from datetime import datetime
import argparse

def generate_id(input_data: dict, model_version: str) -> str:
    payload = f"{json.dumps(input_data, sort_keys=True)}{model_version}{datetime.utcnow().date()}"
    return hashlib.sha256(payload.encode()).hexdigest()[:10]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--model", type=str, required=True)
    args = parser.parse_args()
    
    input_dict = json.loads(args.input)
    pid = generate_id(input_dict, args.model)
    print(f"Prediction ID: {pid}")
