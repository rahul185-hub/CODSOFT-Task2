Name: Rahul Bisht 
Domain: Machine Learning 


# 💳 Credit Card Fraud Detection using Machine Learning

A Machine Learning project that predicts whether a credit card transaction is **Fraudulent** or **Legitimate** using the **LightGBM** algorithm. The project also includes a **Streamlit** web application for an interactive user experience.

---

## 📌 Project Overview

Credit card fraud is a major challenge in the banking industry. This project uses a trained Machine Learning model to detect fraudulent transactions based on historical transaction data.

The application allows users to:
- Select a transaction by entering its row number.
- View the transaction details.
- Predict whether the transaction is Fraud or Legitimate.
- Display the fraud probability.
- Compare the prediction with the actual class.

---

## 🚀 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- LightGBM
- Streamlit
- Joblib
- Matplotlib
- Seaborn

---

## 📂 Project Structure

```
Credit_Card_Fraud_Detection/
│
├── app.py              # Streamlit web application
├── app.ipynb           # Model training notebook
├── model.pkl           # Trained LightGBM model
├── scaler.pkl          # Saved scaler for Amount feature
├── requirements.txt    # Required Python packages
├── README.md           # Project documentation
└── dataset.csv         # Dataset (download separately)
```

---

## 📊 Dataset

This project uses the **Credit Card Fraud Detection Dataset** from Kaggle.

**Dataset Link:**

https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

### Dataset Features

- Time
- Amount
- V1 – V28 (anonymized features)
- Class
  - **0** → Legitimate Transaction
  - **1** → Fraudulent Transaction

> **Note:** The features **V1 to V28** are anonymized to protect customer privacy.

---

## ⚙️ Machine Learning Workflow

1. Load the dataset.
2. Preprocess the data.
3. Scale the **Amount** feature.
4. Split the dataset into training and testing sets.
5. Train the **LightGBM** model.
6. Save the trained model using **Joblib**.
7. Build an interactive interface using **Streamlit**.

---

## 💻 Streamlit Application

The Streamlit interface allows users to:

- Enter a transaction row number.
- Automatically load transaction details.
- Predict Fraud or Legitimate.
- View fraud probability.
- Compare with the actual class.

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Credit_Card_Fraud_Detection.git
```

### 2. Open the project folder

```bash
cd Credit_Card_Fraud_Detection
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Download the dataset

Download **dataset.csv** from Kaggle and place it in the project folder.

### 7. Run the application

```bash
streamlit run app.py
```

---

## 📷 Screenshots

![Uploading image.png…]()


## 📈 Model

- Algorithm: **LightGBM**
- Output:
  - Legitimate Transaction
  - Fraudulent Transaction
- Displays fraud probability.

---

## 📖 Learning Outcome

Through this project, I learned:

- Data preprocessing
- Feature scaling
- Machine Learning model training
- Model serialization using Joblib
- Building interactive applications with Streamlit
- Credit card fraud detection using supervised learning

---

## 👨‍💻 Author

**Rahul**

GitHub: https://github.com/rahul185-hub

---

## ⭐ If you like this project

Please consider giving this repository a ⭐ on GitHub!
