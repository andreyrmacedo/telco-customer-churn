# 📊 Customer Churn Prediction - ML Case Study


## Live Project

Explore the full interactive report:

👉 **[View on GitHub Pages](https://andreyrmacedo.github.io/telco-customer-churn/)**  

> ⚠️ *Note:* Plotly visualizations are fully rendered in this version.  
> GitHub’s notebook preview does not support interactive charts.

---


## Business Problem

Customer churn is one of the most critical challenges for subscription-based businesses.

> Acquiring a new customer usually costs much more than retaining an existing one.

The goal of this project is to:
- Identify customers at risk of churning  
- Understand the drivers behind churn  
- Enable targeted retention strategies  


---


## Exploratory Data Analysis

Key findings:
- 📉 Short-tenure customers are significantly more likely to churn  
- 📄 Contract type strongly influences retention  
- 💳 Billing structure correlates with churn behavior  


---


## Models

Models evaluated:
- Logistic Regression (baseline & tuned)
- Random Forest (baseline & tuned)
- Gradient Boosting (baseline & tuned)
- XGBoost (baseline & tuned)
- Voting Classifier - ensemble learning


---


## Evaluation Strategy

| Metric | Why it matters |
|------|----------------|
| AUC | Overall model discrimination |
| F1-score (Churn) | Balance between recall & precision |
| Recall (Churn) | Minimize missed churners |


---


## Final Recommendation

#### 🥇 Voting Classifier 2 

#### 🥈 Logistic Regression (CV) - Best for Churn Detection

**Use Voting Classifier 2 in production**, because of its strong overall performance and balanced metric.


---


## Next Steps 

- Optimize decision threshold based on business cost  
- Quantify ROI of retention campaigns  
- Develop customer segmentation strategies
- Extend the analysis using survival analysis
- Design retention campaigns


---


## 📁 Project Structure

telco-customer-churn/
├── data/
├── index.html
├── preprocess_data.py
├── README.md
├── requirements.txt
├── telco_customer_churn.ipynb
└── utils.py