# co2-emissions-prediction
# 🌍 CO₂ Emissions Prediction Using Time Series Models

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Published](https://img.shields.io/badge/Published-Microcomputer%20Applications%202024-green?style=flat)](https://www.microapp.com.cn/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat)](LICENSE)

> **Published in:** *Microcomputer Applications*, September 2024, Issue 944, ISSN 1002-140X  
> **Author:** Zhetao Zhang | University of North Carolina at Chapel Hill

---

## 📌 Overview

This project predicts the monthly average atmospheric CO₂ concentration
at the **Mauna Loa Observatory** for April 2024, using historical data
from **March 1958 to March 2024** provided by NOAA.

We compare four time series models and identify the best performer:

| Model | Test MSE | Rank |
|-------|----------|------|
| LSTM | Lowest ✅ | 🥇 Best |
| Polynomial + Harmonic | Low | 🥈 2nd |
| ARIMA(1,1,1) | Medium | 🥉 3rd |
| SARIMA(1,1,1)(1,0,0,12) | Highest | 4th |

### 🎯 Key Result
> **Predicted April 2024 CO₂:** `427.27 ppm`  
> **95% Prediction Interval:** `(424.95, 428.15) ppm`

---

## 📁 Repository Structure
---

## 🚀 How to Run

**1. Clone the repository**
```bash
git clone https://github.com/TaoMay/co2-emissions-prediction.git
cd co2-emissions-prediction
```

**2. Install dependencies**
```bash
pip install pandas numpy matplotlib statsmodels scikit-learn tensorflow
```

**3. Run the notebook**
```bash
jupyter notebook co2_emissions_prediction.ipynb
```

Or run the Python scripts directly:
```bash
python main.py
```

---

## 📊 Results

### Model Comparison — Forecast vs Actual

![Model Comparison](model_comparison.png)

### CO₂ Trend (1958–2024)

![EDA](co2_eda.png)

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat&logo=tensorflow&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)

---

## 📚 Data Source

- **NOAA Global Monitoring Laboratory** — Mauna Loa CO₂ monthly averages  
- URL: https://gml.noaa.gov/ccgg/trends/

---

## 📖 Publication

> Zhang, Z. (2024). *A Model for CO₂ Emissions Prediction Based on
> Historical Data*. Microcomputer Applications, Issue 944, ISSN 1002-140X.

---

## 👤 Author

**Zhetao Zhang**  
MS in Applied Data Science — University of Chicago  
BS in Mathematics & Statistics — UNC Chapel Hill  
📧 zztao@uchicago.edu
