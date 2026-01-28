# Enterprise AI Dashboard: Sales Forecasting & Strategic Insights

<div align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/2103/2103633.png" width="120">
  <h1>Hybrid Business Intelligence System</h1>
  <p><b>Predictive Modeling (Random Forest) + Time-Series Analytics (SARIMA)</b></p>
</div>

---

<div align="center">
  <a href="https://businessforecasting-kzns6cgs9dtvqxclei8z39.streamlit.app/">
    <img src="https://img.shields.io/badge/Streamlit-Live%20App-ff4b4b?style=for-the-badge&logo=streamlit" alt="Live App">
  </a>
</div>

## 📌 Executive Summary
This project presents a comprehensive financial analysis of monthly business data from **2000 to 2005**. The primary objective was to engineer a system that understands the core drivers of profitability and projects performance for the fiscal year **2006**.

### 🛠️ Key Strategic Findings
* **Driver-Based Accuracy:** The system identifies 'Quantity' and 'Cost' as the main engines of profit, achieving **87% accuracy** via Regression.
* **Stationarity & Health:** The **Augmented Dickey-Fuller (ADF) Test** confirmed data stability, allowing for reliable long-term forecasting.
* **Future Projection:** The model forecasts a total annual profit of **£496,436.43** for the next 12 months.

---

## 🧠 Machine Learning Architecture

### A. Operational Layer: Multi-Output Random Forest
Unlike traditional single-variable models, this layer predicts **Revenue and Profit** simultaneously.
* **Technality:** Utilizes an ensemble of 100+ Decision Trees to capture non-linear relationships between unit price-points and sales volume.
* **Significance:** Proves that profit is heavily influenced by the quantity-to-cost ratio.



### B. Strategic Layer: SARIMA Forecasting
To handle the "seasonal rhythm" of the business, we implemented **SARIMA(1, 1, 1)x(1, 1, 1, 12)**.
* **Logic:** Decomposition revealed clear seasonal patterns where profit fluctuates at specific intervals.
* **Risk Mitigation:** The dashboard visualizes **95% Confidence Intervals**, providing stakeholders with a "Safety Range" for financial planning.



---

## 📊 Technical Specifications & Data Engineering
* **Dataset:** 1,001 historical records with 7 transactional features.
* **Normalization:** Applied **StandardScaler** (Z-score normalization) to ensure the AI remains unbiased across different feature scales.
* **Performance Metrics:**
    * **Regression Accuracy:** 87%
    * **SARIMA Final Accuracy:** 55.26% (Optimized for high-variance retail environments).

## 📂 Repository Breakdown
* `app.py`: Deployment logic and interactive dashboard engine.
* `ui.py`: Premium CSS components and visual analytics logic.
* `Forecasting_using_SARIMA.ipynb`: Experimental research and model tuning.
* `df_sarima.csv`: Cleaned transactional data.

## 🏁 Final Conclusion
The analysis confirms that while time-based trends provide a roadmap, **Sales Quantity** is the true growth engine. To maximize the projected **£496K profit**, the business should focus on volume optimization during the seasonal peaks identified by the SARIMA model.

---
**Developed by Shoukat Ali** | *Transforming Business Data into Strategic Intelligence.*