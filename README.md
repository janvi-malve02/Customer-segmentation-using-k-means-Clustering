<h1 align="center">🛍️ Customer Segmentation using K-Means Clustering</h1>

<p align="center">
  Grouping online retail customers into meaningful segments from transaction data, with an interactive <b>Streamlit</b> app.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white" alt="scikit-learn">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white" alt="Pandas">
</p>

---

## 🔎 Overview

Treating every customer the same wastes marketing effort. This project applies **unsupervised learning (K-Means clustering)** to retail transaction data to discover groups of customers with similar purchasing behaviour, so a business can treat each group differently: reward loyal buyers, win back inactive ones, and nurture new ones.

**Goals**
- Turn raw transaction records into customer-level behavioural features
- Group customers with K-Means clustering
- Interpret each group in plain business terms
- Present the result through an interactive Streamlit app

## 🎬 Demo

A screen recording of the Streamlit app is included in this repository:
[▶️ Watch the Streamlit demo](Streamlit%20-%20Google%20Chrome%202026-04-14%2015-54-42.mp4)

## 📊 Dataset

| Property | Details |
|----------|---------|
| Name | **Online Retail II** |
| Source | Kaggle (originally from the UCI Machine Learning Repository) |
| Content | Transactions of a UK-based online retailer, December 2009 to December 2011 |
| Size | Over one million transaction records |

Raw transactions are aggregated to **one row per customer** before clustering.

## 🧪 Approach

```
Raw transactions → Data cleaning → Customer-level features → Scaling → K-Means clustering → Segment profiling → Streamlit app
```

1. **Data cleaning:** prepare the raw transaction data for analysis
2. **Feature engineering:** summarise each customer's purchasing behaviour
3. **Scaling:** put features on a comparable scale, since K-Means is distance-based
4. **Clustering:** group customers with K-Means
5. **Profiling:** describe each cluster by its typical behaviour
6. **App:** explore the segments interactively with Streamlit

## 💡 How Businesses Can Use Segments

- **High-value, frequent customers:** loyalty rewards and early access to new products
- **Recently active, low-spend customers:** upsell and cross-sell offers
- **Lapsed customers:** targeted win-back campaigns

## ⚠️ Limitations

- K-Means assumes roughly spherical clusters and is sensitive to scaling and outliers
- Choosing the number of clusters involves judgment, and different choices give different segments
- The data covers one retailer between 2009 and 2011, so results may not generalise to other businesses or periods
- Segments are descriptive and have not been validated against real campaign outcomes

## 🚀 Future Work

- [ ] Compare K-Means with other methods (DBSCAN, hierarchical clustering, Gaussian mixture models)
- [ ] Add a predictive layer such as churn or customer lifetime value
- [ ] Deploy the Streamlit app online for a live demo link
- [ ] Track how customers move between segments over time

## 🏁 Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/janvi-malve02/Customer-segmentation-using-k-means-Clustering.git
cd Customer-segmentation-using-k-means-Clustering

# 2. Install dependencies
pip install -r requirements.txt
```

3. Download the **Online Retail II** dataset from Kaggle.
4. Open the project folder and run the notebook or the Streamlit app.

## 🛠️ Tech Stack

Python · Pandas · NumPy · scikit-learn · Matplotlib · Seaborn · Streamlit

## 👩‍💻 Author

**Janvi Malve** | [GitHub](https://github.com/janvi-malve02) | [LinkedIn](https://www.linkedin.com/in/janvi-malve) | janvimalve12@gmail.com
