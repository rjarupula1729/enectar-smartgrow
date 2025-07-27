# pages/2_Recommendations.py

import streamlit as st
import pandas as pd

st.title("🤖 Smart Plant Recommendations")

df = pd.read_csv("data/plant_db.csv")

# Inputs from user
light = st.selectbox("🌞 Sunlight", ["full", "partial"])
water = st.selectbox("💧 Water Need", ["low", "medium", "high"])
space = st.selectbox("🏡 Space Available", ["balcony", "terrace", "indoor", "window"])

# Filter and recommend
filtered = df[
    (df["light"] == light) &
    (df["water"] == water) &
    (df["space"].str.contains(space))
]

if not filtered.empty:
    st.success("🌿 Recommended Plants:")
    for _, row in filtered.iterrows():
        st.markdown(f"""
        - **{row['plant_name']}**  
        Care Tip: _{row['care_tips']}_  
        Benefits: _{row['benefits']}_
        """)
else:
    st.warning("No exact match found. Try adjusting preferences.")
