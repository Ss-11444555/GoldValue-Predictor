# Risk Register – Week 06 (GoldValue-Predictor)

| Risk ID | Description                                  | Category    | Likelihood (L) | Impact (I) | Score (L×I)  | Response   |
|---------|----------------------------------------------|-------------|----------------|------------|--------------|------------|
| R1      | Dataset too small or inconsistent            | Technical   | 3              | 4          | 12           | Mitigate   |
| R2      | Model accuracy lower than expected           | Technical   | 4              | 5          | 20           | Reduce     |
| R3      | GPU hours exceed allocated budget            | Cost        | 4              | 4          | 16           | Reduce     |
| R4      | Schedule delays due to extra tuning          | Schedule    | 3              | 3          | 9            | Accept     |
| R5      | Difficulty generating clear visualizations   | Technical   | 2              | 3          | 6            | Mitigate   |
| R6      | Miscommunication about task deadlines        | Stakeholder | 2              | 4          | 8            | Improve communication |
| R7      | Tool or library version conflicts            | Resource    | 3              | 3          | 9            | Mitigate   |

---

# Top Priority Risks (Mitigation Plans)

### **1. R2 – Model accuracy lower than expected (Score 20)**
- **Mitigation:** Try multiple algorithms, tune hyperparameters, and improve feature engineering.
- **Owner:** Mohammed
- **Deadline:** 12 Dec

### **2. R3 – GPU hours exceed allocated budget (Score 16)**
- **Mitigation:** Limit training epochs, monitor cloud usage, run offline tests first.
- **Owner:** Husam
- **Deadline:** 10 Dec

### **3. R1 – Dataset too small or inconsistent (Score 12)**
- **Mitigation:** Add supplemental datasets, check for missing dates, smooth anomalies.
- **Owner:** Zayed
- **Deadline:** 8 Dec

---

## Integration Notes

- High-risk tasks identified mainly in Phase 2 (data preparation) and Phase 3 (model training).
- Risk checks will be performed before training begins and after evaluation.
- Schedule updated to include mitigation time for R1, R2, and R3.
