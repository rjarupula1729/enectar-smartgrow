import streamlit as st
import json
import datetime

# Load plant data
def load_plants_data():
    with open(".\data\plants_db.json", "r") as file:
        return json.load(file)

plants = load_plants_data()
plant_names = [plant["name"] for plant in plants]

st.title("🌱 Plant Tracker")

# Dropdown to select a plant
selected_plant_name = st.selectbox("Select a Plant to Track", plant_names)

# Get selected plant details
selected_plant = next((plant for plant in plants if plant["name"] == selected_plant_name), None)

if selected_plant:
    st.subheader(f"🌿 {selected_plant['name']} Details")

    col1, col2 = st.columns(2)

    with col1:
     #   st.markdown(f"**🗺️ Location(s):** {', '.join(selected_plant['location'])}")
        st.markdown(f"**☀️ Sunlight:** {', '.join(selected_plant['sunlight'])}")
        st.markdown(f"**💧 Water Needs:** {', '.join(selected_plant['water'])}")
        st.markdown(f"**🌡️ Season:** {selected_plant['season']}")
    #   st.markdown(f"**👨‍👩‍👧 Ideal for Family Size:** {selected_plant['family_size']}")

    with col2:
     #   st.markdown(f"**🌱 Growth Stage:** {selected_plant['growth_stage']}")
        st.markdown(f"**🛠️ Care Instructions:** {selected_plant['care']}")
        st.markdown(f"**🌿 Health Benefits:** {selected_plant['uses']}")
     #   st.markdown(f"**🍽️ Uses:** {selected_plant['uses']}")

    st.divider()
    st.subheader("📅 Planting Tracker")
    
    # User can enter the planting date
    planting_date = st.date_input("Select Planted On Date", datetime.date.today())
    
    # Placeholder for DB storing functionality
    if st.button("✅ Submit"):
        st.success(f"{selected_plant['name']} planted on {planting_date} has been recorded.")
        # Future scope: Store in database

