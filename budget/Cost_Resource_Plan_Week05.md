# Week 05 – Cost & Resource Plan
Project: GoldValue-Predictor

## 1. Resources per WBS Task

| WBS ID | Task                        | Resource Type | Resource Name      | Hours/Qty | Description                          |
|--------|-----------------------------|---------------|--------------------|-----------|--------------------------------------|
| 1.1    | Define problem & objectives | Human         | Student (Self)     | 3 hrs     | Reading requirements and scoping     |
| 2.1    | Collect gold price data     | Human         | Student (Self)     | 5 hrs     | Searching and downloading datasets   |
| 2.2    | Clean & preprocess dataset  | Software      | Python, Pandas     | —         | Data cleaning tools                  |
| 2.3    | Feature engineering         | Human         | Data Analyst role  | 4 hrs     | Create new features                  |
| 3.1    | Train ML model              | Hardware      | GPU / CPU Instance | 8 hrs     | Training regression model            |
| 3.2    | Evaluate model              | Human         | ML Engineer role   | 4 hrs     | Calculate MAE, RMSE, MAPE            |
| 3.3    | Visualize results           | Software      | Matplotlib, Excel  | —         | Plots and charts                     |
| 4.1    | Write final report          | Human         | Student (Self)     | 6 hrs     | Writing analysis and conclusion      |
| 4.2    | Prepare presentation slides | Human         | Student (Self)     | 4 hrs     | Slide preparation                    |

## 2. Task Cost Estimation

_Assumed rates:_
- Student / team member: **RM 25/hour**
- Specialist role (Data Analyst / ML Engineer): **RM 30/hour**
- GPU/Cloud instance: **RM 10/hour**

| Task                          | Hours | Rate (RM/hr) | Total Cost (RM) |
|-------------------------------|-------|--------------|------------------|
| Define problem & objectives   | 3     | 25           | 75               |
| Collect gold price data       | 5     | 25           | 125              |
| Feature engineering           | 4     | 30           | 120              |
| Train ML model (GPU)          | 8     | 10           | 80               |
| Model evaluation              | 4     | 30           | 120              |
| Final report writing          | 6     | 25           | 150              |
| Presentation preparation      | 4     | 25           | 100              |
| **Total**                     | —     | —            | **770**          |

## 3. Budget Summary

| Cost Category        | Items Included                     | Subtotal (RM) |
|----------------------|------------------------------------|---------------|
| Human Resources      | Student work, analyst, ML engineer | 570           |
| Hardware / Cloud     | GPU / CPU instance                 | 80            |
| Software / Licenses  | Python, libraries (assumed free)   | 0             |
| Communication / Misc | Meetings, internet, printing       | 120           |
| **Total Budget**     |                                    | **770**       |

## 4. Integration Notes

The highest cost is human resources, especially feature engineering, evaluation, and reporting. GPU usage also contributes to the cost during model training. These costs align with milestones such as “Data Preparation Complete” and “Model Trained & Evaluated”. If the budget becomes tight, time on GPU can be reduced and more effort can be spent on efficient feature engineering and model selection.
