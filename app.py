import streamlit as st
import pandas as pd
import joblib

# Load model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# Load dataset
df = pd.read_csv("dataset.csv")

st.title("💳 Credit Card Fraud Detection")

# Enter row number
row = st.number_input(
    "Enter Transaction Row Number",
    min_value=0,
    max_value=len(df)-1,
    value=0,
    step=1
)

# Automatically load the selected row
sample = df.iloc[int(row)]

st.subheader("Transaction Details")
st.dataframe(sample.to_frame().T)

# Predict button
if st.button("Predict"):

    X = sample.drop("Class").to_frame().T

    # Scale Amount
    X["Amount"] = scaler.transform(X[["Amount"]])

    prediction = model.predict(X)[0]
    probability = model.predict_proba(X)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("🚨 Fraud Transaction")
    else:
        st.success("✅ Legitimate Transaction")

    st.metric("Fraud Probability", f"{probability*100:.2f}%")

    actual = "Fraud" if sample["Class"] == 1 else "Legitimate"

    st.write("### Actual Class")
    st.write(actual)