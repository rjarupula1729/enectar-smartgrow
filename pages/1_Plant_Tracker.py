# pages/1_Plant_Tracker.py

import streamlit as st
import pandas as pd
import datetime
import os

st.title("🌱 Plant Growth Tracker")

DATA_FILE = "data/plant_growth_log.csv"

# Initialize file
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=["Date", "Plant Name", "Height (cm)", "Notes"])
    df.to_csv(DATA_FILE, index=False)

# Load data
df = pd.read_csv(DATA_FILE)

# Input form
with st.form("growth_form"):
    date = st.date_input("Date", datetime.date.today())
    name = st.text_input("Plant Name")
    height = st.number_input("Plant Height (cm)", min_value=0.0)
    notes = st.text_area("Notes")
    submitted = st.form_submit_button("Save Record")

    if submitted:
        new_entry = pd.DataFrame([[date, name, height, notes]],
                                 columns=df.columns)
        df = pd.concat([df, new_entry], ignore_index=True)
        df.to_csv(DATA_FILE, index=False)
        st.success("🌿 Record Saved!")

# View growth logs
st.subheader("📈 Growth Log")
st.dataframe(df)

if not df.empty:
    st.line_chart(df.groupby("Date")["Height (cm)"].mean())
