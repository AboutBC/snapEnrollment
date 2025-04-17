# 📊 SNAP Enrollment Forecasting by County

This project builds an end-to-end machine learning pipeline to forecast **SNAP (Supplemental Nutrition Assistance Program)** participation rates across U.S. counties using publicly available government data.

It combines data engineering, feature engineering, modeling, and interactive dashboarding to explore how economic and demographic trends influence food assistance enrollment.

---

## 🧠 Project Goals

- Predict SNAP enrollment by U.S. county using Census, BLS, and USDA data
- Build a reproducible ETL pipeline using APIs and automation
- Apply ML models (e.g., XGBoost, ElasticNet) for accurate predictions
- Visualize predictions and feature impacts with SHAP + dashboards

---

## 🗂️ Project Structure

```bash
snap-enrollment-prediction/
├── data/                 # Raw and processed datasets
├── notebooks/            # Exploratory notebooks
├── src/                  # Source code (see breakdown below)
│   ├── etl/              # Data extraction and loading scripts
│   ├── features/         # Feature engineering and cleaning
│   ├── modeling/         # ML training, prediction, and evaluation
│   ├── visualization/    # Plotting and dashboarding tools
│   └── utils/            # Configs, helpers, and logging
├── api/                  # Optional FastAPI app to serve predictions
│   ├── main.py               # Main FastAPI app
│   ├── predict.py            # Loads model and makes predictions
│   ├── model/                # Serialized model files (e.g., .pkl or .joblib)
│   └── schemas.py            # Pydantic input/output validation
├── dbt/                  # (Optional) dbt transformations if using SQL [least likely]
│   ├── dbt_project.yml         # Project config
│   ├── models/
│   │   ├── staging/            # Clean raw tables
│   │   ├── marts/              # Final, analysis-ready tables
│   │   └── snap_forecast.sql   # SQL model to create features
│   ├── seeds/                  # Static CSVs loaded into DB
│   └── snapshots/              # Historical change tracking (optional)
├── requirements.txt      # Python package dependencies
├── README.md             # Project overview and documentation
└── streamlit_app.py      # Streamlit dashboard entry point
