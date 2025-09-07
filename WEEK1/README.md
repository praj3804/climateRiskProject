# 🌍 Climate Risk Analysis Project  

## 📅 Week 1 & Week 2 Progress  

This project analyzes **historical climate data** to identify trends, anomalies, and risks associated with climate change.  
The goal is to better understand **temperature, rainfall, and extreme weather patterns**, and to assess how these changes might impact ecosystems, agriculture, and human livelihoods.  

By using Python (`Pandas`, `Matplotlib`, `Seaborn`, `Scikit-learn`), the project performs **data cleaning, exploratory data analysis (EDA), feature selection, and visualization of climate patterns**.  

---

## 🎯 Objectives

* Analyze historical weather data (temperature, precipitation, humidity, wind speed, etc.).  
* Identify seasonal patterns and long-term trends.  
* Detect extreme events (heatwaves or coldwaves).  
* Provide visual insights (line plots, heatmaps, bar charts).  
* Support climate risk assessment for decision-making.  

---

## 🗂️ Dataset

The dataset contains historical climate information, including:  

* **Temperature** (min, max, average)  
* **Precipitation**  
* **Humidity**  
* **Wind Speed**  
* **Weather Condition**  

📌 Source: [Kaggle – Historical Weather Data (2020)](https://www.kaggle.com/datasets/ahmedgaitani/historical-weather-data-for-2020)  

---

## 🛠️ Tech Stack

* Language: **Python**  
* Libraries:  
  * `pandas` → Data handling  
  * `numpy` → Numerical analysis  
  * `matplotlib` & `seaborn` → Visualization  
  * `scikit-learn` → Machine learning for feature selection and anomaly detection  
* Environment: **VS Code / Jupyter Notebook**  

---

## 🚀 Project Workflow  

### ✅ Week 1 – Data Understanding  
1. **Data Collection** → Imported dataset (`.csv`) from Kaggle.  
2. **Data Inspection** → Shape, info, and descriptive statistics.  
3. **Data Cleaning** → Checked for missing values and basic inconsistencies.  
4. **Initial EDA** →  
   - Histograms of numerical features.  
   - Identified min/max temperature values (range: -9°C to 34°C).  
5. **Week 1 Conclusion** →  
   - Dataset contained 1095 rows and 7 columns.  
   - No major missing values detected.  
   - Data ready for further transformation and modeling.  

---

### ✅ Week 2 – Advanced EDA, Transformation & Feature Selection  
1. **Exploratory Data Analysis (EDA)** →  
   - Correlation heatmap of numerical features.  
   - Boxplots to identify outliers.  
   - Time-series visualization of temperature trends.  

2. **Data Transformation** →  
   - Filled missing values using median.  
   - Outlier removal using **IQR method**.  
   - Normalized data using **MinMaxScaler** for better modeling.  

3. **Feature Selection** →  
   - Implemented **RandomForestRegressor** to identify feature importance.  
   - Found **Humidity** and **Precipitation** as strong predictors for temperature.  

4. **Week 2 Conclusion** →  
   - Relationships between variables visualized using heatmaps & scatterplots.  
   - Outliers handled, dataset normalized, and features ranked.  
   - Dataset now ready for **Week 3 (feature engineering & model building)**.  

---

## 📊 Visuals Included
- Distribution plots (histograms).  
- Correlation heatmap.  
- Boxplots for outlier detection.  
- Time-series plot of temperature.  
- Feature importance bar chart (Random Forest).  

---


