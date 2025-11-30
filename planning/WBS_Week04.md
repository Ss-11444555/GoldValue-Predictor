# Week 04 – Work Breakdown Structure (WBS)
## Project: GoldValue-Predictor – Machine Learning Model for Predicting Gold Prices

---

## Major Phases
1. Data Acquisition & Cleaning  
2. Exploratory Analysis & Feature Engineering  
3. Model Development & Evaluation  
4. System Deployment & Documentation  

---

## Subtasks

| WBS ID | Phase                               | Task                                                               | Deliverable                                   | Owner      | Start       | End         |
|--------|---------------------------------------|---------------------------------------------------------------------|-------------------------------------------------|------------|-------------|-------------|
| 1.1    | Data Acquisition & Cleaning           | Collect historical gold price datasets (CSV/API)                   | Raw data in `/data/raw/`                       | Mohammed   | 24 Nov 2025 | 25 Nov 2025 |
| 1.2    | Data Acquisition & Cleaning           | Clean missing values, merge datasets, handle anomalies             | Clean dataset in `/data/processed/`            | HUSAM   | 25 Nov 2025 | 27 Nov 2025 |
| 1.3    | Data Acquisition & Cleaning           | Perform feature extraction (e.g., moving averages)                 | Feature-enhanced dataset                       | ZAYED   | 27 Nov 2025 | 28 Nov 2025 |

| 2.1    | Exploratory Analysis & Engineering    | Build EDA notebook (trends, seasonality, correlations)             | Notebook in `/notebooks/EDA.ipynb`             | AMIR   | 28 Nov 2025 | 29 Nov 2025 |
| 2.2    | Exploratory Analysis & Engineering    | Create feature engineering pipeline                                 | Feature pipeline script in `/src/`            | Mohammed   | 29 Nov 2025 | 30 Nov 2025 |

| 3.1    | Model Development & Evaluation        | Train ML models (Linear Regression, RandomForest, XGBoost, etc.)   | Model training notebook in `/notebooks/`       | AMIR   | 30 Nov 2025 | 01 Dec 2025 |
| 3.2    | Model Development & Evaluation        | Evaluate models (RMSE, MAPE, R²)                                   | Evaluation report in `/reports/`               | ZAYED   | 01 Dec 2025 | 03 Dec 2025 |
| 3.3    | Model Development & Evaluation        | Select best-performing model and export `.pkl`                     | Best model file in `/src/model/`               | Mohammed   | 03 Dec 2025 | 04 Dec 2025 |

| 4.1    | System Deployment & Documentation     | Build prediction pipeline (input → preprocessing → model → output) | Pipeline script in `/src/`                     | HUSAM   | 04 Dec 2025 | 05 Dec 2025 |
| 4.2    | System Deployment & Documentation     | Write technical documentation & API description                    | Docs in `/docs/`                               | HUSAM   | 05 Dec 2025 | 06 Dec 2025 |
| 4.3    | System Deployment & Documentation     | Final report & presentation                                        | Final files in `/reports/`                     | HUSAM   | 06 Dec 2025 | 07 Dec 2025 | 

---

## Deliverables (GitHub Aligned)

- `/data/raw/` – Original gold price datasets  
- `/data/processed/` – Clean & engineered datasets  
- `/notebooks/EDA.ipynb` – Exploratory analysis  
- `/notebooks/Model_Training_GoldValue.ipynb` – Training & evaluation  
- `/src/pipeline.py` – Prediction pipeline  
- `/src/model/best_model.pkl` – Saved ML model  
- `/docs/system_architecture.png` – Architecture  
- `/reports/model_evaluation_report.md` – Model evaluation  
- `/reports/final_report.md` – Final written report  

---

## Milestones
- **Data Preparation Complete** – 28 Nov 2025  
- **Model Development Complete** – 04 Dec 2025  
- **System Pipeline + Documentation Complete** – 07 Dec 2025  
- **Project Ready for Submission** – 07 Dec 2025  


