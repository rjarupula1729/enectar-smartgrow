# GrowPal_Connect.py

import streamlit as st
import json

#st.set_page_config(page_title="GrowPal Connect", layout="wide")
def main(): 
    st.title("🌱 GrowPal Connect – Support & Earn with Your Plant Knowledge")

    menu = st.radio("Select Option", ["📋 Become a GrowPal (Mentor)", "🔍 Find a GrowPal (Get Help)"])

    if menu == "📋 Become a GrowPal (Mentor)":
        st.subheader("🧑‍🌾 Register as a Certified Gardening Mentor")

        name = st.text_input("Full Name")
        expertise = st.multiselect("Expertise Areas", ["Soil Gardening", "Hydroponics", "Vertical Farming", "Composting", "Plant Health", "Beginner Gardening"])
        location = st.text_input("City / Region")
        certification = st.file_uploader("Upload Certification or Badge (PDF/Image)", type=["pdf", "png", "jpg"])
        availability = st.text_input("Available Time Slots (e.g., Weekends 10AM–2PM)")
        charge = st.number_input("Your Charge per Session (₹)", min_value=0)

        if st.button("Register"):
            mentor_data = {
                "name": name,
                "expertise": expertise,
                "location": location,
                "availability": availability,
                "charge": charge
            }
            # Save data (For now, just show confirmation)
            st.success(f"Thank you {name}! You've been registered as a GrowPal Mentor.")
            st.json(mentor_data)

    elif menu == "🔍 Find a GrowPal (Get Help)":
        st.subheader("🧑‍🌱 Need help with gardening? Find a GrowPal nearby!")

        your_location = st.selectbox("Your Location", ["Hyderabad", "Bangalore", "Delhi", "Mumbai", "Chennai", "Other"])
        grow_method = st.selectbox("Preferred Growing Method", ["Soil", "Hydroponic", "Vertical Farming"])

        # Dummy mentor listing for UI preview
        st.write("### 🌟 Available Mentors Near You:")
        st.info("""
        👨‍🏫 **Name:** Priya Sharma  
        🌿 **Expertise:** Hydroponics, Beginner Gardening  
        📍 **Location:** Hyderabad  
        🕒 **Available:** Weekends 10AM–2PM  
        💸 **Charge:** ₹200 per session  
        ⭐️ **Rating:** 4.9 / 5
        """)

        if st.button("📩 Request a Session"):
            st.success("Session Request Sent! Mentor will contact you shortly.")

        st.markdown("---")
        st.caption("Note: You will earn loyalty rewards by participating or providing help regularly.")

