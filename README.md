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
