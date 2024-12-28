import streamlit as st
import pickle
import pandas as pd

# Load the model and preprocessor
@st.cache_resource
def load_model():
    try:
        with open("datafile\model.pkl", "rb") as model_file:
            model = pickle.load(model_file)
        with open("datafile\proprocessor.pkl", "rb") as preprocessor_file:
            preprocessor = pickle.load(preprocessor_file)
        return model, preprocessor
    except Exception as e:
        st.error(f"Error loading model or preprocessor: {e}")
        return None, None

# Load model and preprocessor
model, preprocessor = load_model()

# Streamlit App
st.title("Base Price Prediction")

st.write("""
This application predicts the **Base Price** of a product based on:
- Competitor Price
- Profit Margin
- Inventory Level
- Inventory Risk
- Adjusted Elasticity
- Category
- Green Certification Label
- Product Name
""")

# List of product names
product_names = [
    "Solar-Powered Lantern",
    "Eco-Friendly Notebook",
    "Bamboo Toothbrush",
    "Reusable Water Bottle",
    "Compostable Trash Bags",
    "Biodegradable Phone Case",
    "Recycled Paper Planner",
    "Solar Charger",
    "Organic Cotton T-Shirt",
    "Organic Wool Socks"
]

# List of categories
categories = [
    "Electronics",
    "Household",
    "Personal Care",
    "Clothing",
    "Stationery"
]

# List of Green Certification Labels
green_cert_labels = [
    "Certified",
    "Non-Certified"
]

# Check if model and preprocessor loaded successfully
if model is None or preprocessor is None:
    st.error("Failed to load the model or preprocessor. Please check the files in the 'datafile' folder.")
else:
    # Input fields
    competitor_price = st.number_input("Competitor Price ($)", min_value=0.0, format="%.2f")
    profit_margin = st.number_input("Profit Margin (%)", min_value=0.0, max_value=100.0, format="%.2f")
    inventory_level = st.number_input("Inventory Level (units)", min_value=0, format="%d")
    inventory_risk = st.number_input("Inventory Risk (scale 0-1)", min_value=0.0, max_value=1.0, step=0.01, format="%.2f")
    adjusted_elasticity = st.number_input("Adjusted Elasticity", format="%.2f")

    category = st.selectbox("Category", categories)
    green_cert_label = st.selectbox("Green Certification Label", green_cert_labels)
    product_name = st.selectbox("Product Name", product_names)

    # Prediction logic
    if st.button("Predict Base Price"):
        try:
            # Prepare input dataframe
            input_data = pd.DataFrame({
                "Competitor_Price": [competitor_price],
                "Profit_Margin": [profit_margin],
                "Inventory_Level": [inventory_level],
                "Inventory_Risk": [inventory_risk],
                "Adjusted_Elasticity": [adjusted_elasticity],
                "Category": [category],
                "Green_Certification_Label": [green_cert_label],
                "Product_Name": [product_name]
            })

            # Ensure preprocessor is applied correctly
            input_processed = preprocessor.transform(input_data)

            # Predict using the model
            prediction = model.predict(input_processed)

            st.success(f"Predicted Base Price: ${prediction[0]:.2f}")
        except Exception as e:
            st.error(f"Error in prediction: {e}")
