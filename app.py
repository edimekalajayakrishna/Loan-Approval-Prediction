from flask import Flask, render_template, request
import pickle
import pandas as pd
import os

app = Flask(__name__)

# Load pipeline (preprocess + model)
model = pickle.load(open("loan_pipeline.pkl", "rb"))

# Try to derive expected raw input columns from pipeline preprocess step
preprocess = None
numeric_cols = []
categorical_cols = []
try:
    preprocess = model.named_steps.get("preprocess", model.named_steps.get("columntransformer"))
    for name, transformer, cols in preprocess.transformers_:
        if name == "num":
            numeric_cols = list(cols)
        elif name == "cat":
            categorical_cols = list(cols)
except Exception:
    # fallback: if pipeline not present or different structure, try loading feature_columns
    if os.path.exists("feature_columns.pkl"):
        feature_columns = pickle.load(open("feature_columns.pkl", "rb"))
    else:
        feature_columns = []

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        # Prepare input dict for raw pipeline preprocess (use defaults if form fields missing)
        data = {}

        # numeric inputs (convert to float; empty/invalid => 0)
        for col in numeric_cols or ["ApplicantIncome","CoapplicantIncome","LoanAmount","Loan_Amount_Term","Credit_History"]:
            val = request.form.get(col, "")
            try:
                data[col] = float(val) if val != "" else 0.0
            except ValueError:
                data[col] = 0.0

        # categorical inputs (use provided value or a sensible default)
        defaults = {
            "Gender":"Male",
            "Married":"Yes",
            "Dependents":"0",
            "Education":"Graduate",
            "Self_Employed":"No",
            "Property_Area":"Semiurban"
        }
        for col in categorical_cols or list(defaults.keys()):
            data[col] = request.form.get(col, defaults.get(col, ""))

        # Build DataFrame with the raw columns in the expected order
        input_df = pd.DataFrame([data])

        # Ensure all expected columns exist (some pipelines require exact column set)
        if preprocess is not None:
            expected_cols = numeric_cols + categorical_cols
            for c in expected_cols:
                if c not in input_df.columns:
                    input_df[c] = defaults.get(c, 0) if c in defaults else 0

            input_df = input_df[expected_cols]

            # Predict using pipeline (it will do preprocessing internally)
            result = model.predict(input_df)[0]
        else:
            # fallback: model expects already-transformed features (feature_columns)
            # create zero-filled feature vector
            for col in feature_columns:
                if col not in input_df.columns:
                    input_df[col] = 0
            input_df = input_df.reindex(columns=feature_columns, fill_value=0)
            result = model.predict(input_df)[0]

        prediction = "✅ Loan Approved" if result == 1 else "❌ Loan Rejected"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)