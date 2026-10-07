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

## 🎬 Demo

<!-- Drag your Streamlit .mp4 recording into this spot in the GitHub editor. GitHub will upload it and show a playable video here. Then delete this comment. -->

## 📌 Table of Contents
- [Overview](#-overview)
- [Dataset](#-dataset)
- [Methodology](#-methodology)
- [Results](#-results)
- [Streamlit App](#-streamlit-app)
- [Business Insights](#-business-insights)
- [Limitations](#-limitations)
- [Future Work](#-future-work)
- [Getting Started](#-getting-started)
- [Tech Stack](#-tech-stack)

---

## 🔎 Overview

Treating every customer the same wastes marketing effort. This project uses **unsupervised learning (K-Means clustering)** on retail transaction data to discover groups of customers with similar purchasing behaviour, so a business can target each group differently (for example reward loyal buyers, win back inactive ones, and nurture new ones).

**Goals**
- Clean and transform raw transaction data into customer-level features
- Find the right number of clusters and justify the choice
- Describe each segment in plain business language
- Make the result usable through a simple Streamlit app

## 📊 Dataset

| Property | Details |
|----------|---------|
| Name | **Online Retail II** |
| Source | Kaggle (originally from the UCI Machine Learning Repository) |
| Content | Transactions of a UK-based online retailer, December 2009 to December 2011 |
| Size | Over one million transaction records |

Raw transactions were aggregated to **one row per customer** before clustering.

## 🧪 Methodology

```
Raw transactions → Cleaning → Customer-level features → Scaling → K-Means → Evaluation → Segment profiling → Streamlit app
```

1. **Data cleaning:** `FILL: e.g. removed missing customer IDs, cancelled orders, duplicates and negative quantities`
2. **Feature engineering:** `FILL: e.g. Recency, Frequency, Monetary (RFM) per customer`
3. **Scaling:** `FILL: e.g. StandardScaler / log transform to handle skew`
4. **Choosing K:** `FILL: e.g. elbow method and silhouette score`
5. **Clustering:** K-Means with **K = `FILL`**
6. **Profiling:** average feature values per cluster, used to name each segment

## 📈 Results

| Metric | Value |
|--------|-------|
| Number of clusters | `FILL` |
| Silhouette score | `FILL` (remove this row if you did not compute it) |

<!-- Add your plots: elbow curve, cluster scatter plot, segment size chart -->
<!-- ![Elbow Curve](images/elbow.png) -->
<!-- ![Clusters](images/clusters.png) -->

| Segment | Description |
|---------|-------------|
| `FILL: Segment 1 name` | `FILL: one-line behaviour description` |
| `FILL: Segment 2 name` | `FILL: one-line behaviour description` |
| `FILL: add or remove rows to match your K` | |

## 💻 Streamlit App

The project includes an interactive **Streamlit** app (see the demo video above). `FILL: one line on what a user can do, e.g. enter customer values and see which segment they belong to`.

Run it locally:

```bash
streamlit run app.py
```

> If your app file has a different name, change `app.py` to match.

## 💡 Business Insights

Segmentation lets a business act differently per group, for example:

- **High-value, frequent customers:** loyalty rewards and early access
- **Recently active, low-spend customers:** upsell and cross-sell offers
- **Lapsed customers:** targeted win-back campaigns

## ⚠️ Limitations

- K-Means assumes roughly spherical clusters and is sensitive to scaling and outliers
- The choice of K involves judgment; different K values give different segments
- Behaviour is based on one retailer's data from 2009 to 2011, so results may not generalise to other businesses or time periods
- Segments are descriptive, not validated against real campaign outcomes

## 🚀 Future Work

- [ ] Compare with other methods (DBSCAN, hierarchical clustering, Gaussian mixture models)
- [ ] Add a predictive layer such as churn or customer lifetime value
- [ ] Deploy the Streamlit app online for a live demo link
- [ ] Track how customers move between segments over time

## 🏁 Getting Started

```bash
# 1. Clone the repo
git clone https://github.com/janvi-malve02/Customer-segmentation-using-k-means-Clustering.git
cd Customer-segmentation-using-k-means-Clustering

# 2. Install dependencies
pip install -r requirements.txt

# 3. Download the dataset from Kaggle ("Online Retail II") and place it in the project folder

# 4. Open the notebook or run the app
jupyter notebook
streamlit run app.py
```

## 🛠️ Tech Stack

Python · Pandas · NumPy · scikit-learn · Matplotlib · Seaborn · Streamlit

## 👩‍💻 Author

**Janvi Malve** | [GitHub](https://github.com/janvi-malve02) | [LinkedIn](https://www.linkedin.com/in/janvi-malve) | janvimalve12@gmail.com
