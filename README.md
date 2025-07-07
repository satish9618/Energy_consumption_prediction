# ⚡ Energy Consumption Prediction with Linear Regression

This project implements a **Linear Regression** model using **scikit-learn** and an interactive **Streamlit** interface. It predicts energy consumption based on key building parameters such as square footage, number of occupants, appliances used, and average temperature.

---

## 📌 Project Description

The analysis focuses on estimating energy consumption using a custom dataset (`Linear_regression_energy.csv`). The workflow includes:

- Exploratory Data Analysis (EDA)
- Outlier detection using IQR
- Multicollinearity handling using **Variance Inflation Factor (VIF)**
- Model training using **Linear Regression**
- Deployment with **Streamlit** for real-time predictions

---

## 🎯 Learning Highlights

Through this project, I developed hands-on experience in:

- ✅ **Outlier Detection** using IQR method to clean noisy data  
- ✅ **Multicollinearity Analysis** using **VIF**, ensuring independent feature contributions  
- ✅ **Model Evaluation** using R-squared (R²)

---

## 📊 Dataset

- **Name:** `Linear_regression_energy.csv`
- **Features:**
  - `Square Footage`
  - `Number of Occupants`
  - `Appliances Used`
  - `Average Temperature (°C)`
  - `Energy Consumption (target)`
- **Preprocessing Steps:**
  - Null handling
  - Outlier removal
  - Feature scaling (if applicable)
  - Multicollinearity check using VIF

---

## 🖥️ User Interface (Streamlit)

The app interface was built using **Streamlit**, providing:

- 📥 Input fields for all model features
- 📊 Real-time prediction of energy consumption
- ✨ Styled with custom CSS and emojis for an improved user experience

---

## 🤖 Model Info

- **Model Used:** Linear Regression (`sklearn.linear_model.LinearRegression`)
- **Frameworks:** 
  - `pandas`, `numpy`, `matplotlib`, `seaborn` for EDA  
  - `scikit-learn` for ML modeling  
  - `streamlit` for deployment  
- **Feature Selection:** Based on VIF scores
- **Outliers:** Removed using IQR-based method

---

## 🚀 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/satish9618/Energy_consumption_prediction.git
cd Energy_consumption_prediction


# Run the app
streamlit run app.py
