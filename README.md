# Fake-Social-Media-Profile-Detection-
Detects fake Instagram profiles using correlation-based analysis of profile features. Uses a weighted scoring method with threshold tuning to classify profiles as fake or real. Lightweight, interpretable, and model-free approach.
# Correlation-Based Fake Instagram Profile Detection 🚩📱

This capstone project detects potentially fake Instagram profiles using machine learning based on engineered features derived from profile metadata.

## 🧠 Idea

Detect fake accounts **without needing actual images or DMs** — just by analyzing:
- Username structure
- Profile description
- Number of followers/following/posts
- Account privacy
- External links

## 📊 Dataset

Collected from public Instagram profiles (simulated/fetched with ethical scraping or anonymized data). Key features:
- `nums/length username`
- `fullname words`
- `description length`
- `#followers`, `#follows`, `#posts`
- `external URL`, `private`, `no abuse report`
- `fake (label)` ✅

## 📈 Approach

1. **Correlation Analysis**: Identify most predictive features (see heatmap in `reports/`)
2. **Modeling**: Used RandomForestClassifier & LogisticRegression
3. **Validation**: 10-fold cross-validation, F1-score, precision, recall, ROC-AUC
4. **Output**: Predicts whether a given profile is likely fake or genuine

## 🚀 How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Train the model
python src/train_model.py

# Predict using a sample profile
python src/predict.py --input "sample_input.json"
