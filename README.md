# CustomerPulse — Customer Churn Prediction & Retention Intelligence

An end-to-end machine learning system that predicts e-commerce customer churn using RFM analysis, with an interactive Streamlit app and Power BI dashboard for business retention insights.

---

## Problem Statement

An e-commerce company spends ₹500 acquiring each customer. 60% buy once and never return. CustomerPulse identifies which customers are likely to churn — before they leave — so businesses can act proactively with targeted retention offers.

---

## Key Results

| Metric | Value |
|--------|-------|
| Accuracy | 83% |
| Churn Recall | 94% |
| Churn Precision | 68% |
| Customers Analyzed | 3,920 |
| Total Revenue Analyzed | £7.25M |
| Revenue at Risk | £379K |

---

## Tech Stack
Python, Pandas, Scikit-learn, MySQL, SQLAlchemy, Streamlit, Plotly, Power BI, Git

---

## Project Architecture

Raw Data (541,909 rows)
→ MySQL Database
→ SQL EDA
→ Data Cleaning (344,435 rows)
→ RFM Feature Engineering
→ Customer Segmentation (Champions/Loyal/At Risk/Lost)
→ Churn Labeling
→ Random Forest Classifier
→ Streamlit App + Power BI Dashboard
---

## Known Limitations
1. **Mild R_Score leakage** — R_Score derived from Recency which defines churn label
2. **Wholesale buyer outliers** — dataset mixes retail and wholesale customers
3. **Threshold sensitivity** — 90-day churn definition is a business assumption

---

## How to Run
```bash
git clone https://github.com/mehta-rutansh/CustomerPulse.git
cd CustomerPulse
pip install -r requirements.txt
streamlit run app.py
```

---


## Author
## Author

Built by **Rutansh Mehta**, an aspiring Data Scientist passionate about machine learning and business analytics.

I built CustomerPulse to showcase how predictive analytics can help businesses identify customer churn early and improve customer retention through data-driven insights.
