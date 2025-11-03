

```markdown
# Layer 1 – Explainability

## SHAP Values
```python
import shap
explainer = shap.Explainer(model)
shap_values = explainer(X)
shap.plots.waterfall(shap_values[0])
