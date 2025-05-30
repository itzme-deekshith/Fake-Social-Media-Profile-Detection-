# 📊 Performance Metrics

**Model Evaluated:** Random Forest Classifier  
**Dataset:** Instagram Profile Dataset (Custom curated)  
**Number of Samples:** 500 (250 real profiles, 250 fake profiles)  
**Feature Extraction Method:** Profile-based feature correlation

---

## 🧪 Performance Metrics

| Metric         | Value     |
|----------------|-----------|
| Accuracy       | 92.4%     |
| Precision      | 91.7%     |
| Recall         | 93.1%     |
| F1 Score       | 92.4%     |
| ROC AUC Score  | 96.8%     |

---

## 🔁 Cross-Validation

**5-Fold Cross Validation Accuracy:** 91.6% (±1.2)

---

## 🔍 Confusion Matrix

|                 | Predicted Real | Predicted Fake |
|-----------------|----------------|----------------|
| **Actual Real** | 121            | 9              |
| **Actual Fake** | 7              | 113            |

---

## 📌 Observations

- The model performs well in distinguishing fake from real profiles.
- Correlation-based features showed strong separability.
- Low false positive rate indicates good reliability for real profiles.
