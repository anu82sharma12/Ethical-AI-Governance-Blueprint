# tools/explain_shap.py
import shap
import joblib
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--model", type=str, default="model/xgb.pkl")
parser.add_argument("--id", type=str, required=True)
args = parser.parse_args()

model = joblib.load(args.model)
X = pd.read_csv("data/sample_input.csv")

explainer = shap.Explainer(model)
shap_values = explainer(X)

print(f"SHAP for Prediction ID: {args.id}")
shap.plots.waterfall(shap_values[0], show=False)
import matplotlib.pyplot as plt
plt.savefig(f"shap_{args.id}.png")
print(f"Saved: shap_{args.id}.png")
