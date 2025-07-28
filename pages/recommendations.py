import streamlit as st
import random
from datetime import date
import datetime
import os, json


# Gardening Tips
DAILY_TIPS = [
        "💧 Water your plants early in the morning to reduce evaporation and prevent fungal growth.",
        "✂️ Prune dead leaves regularly to promote healthy and bushy plant growth.",
        "☀️ Ensure your plants get enough sunlight, but shield them from harsh midday heat.",
        "🛡️ Use neem oil as a natural and effective way to keep pests at bay.",
        "🍂 Apply mulch to retain soil moisture, suppress weeds, and protect roots.",
        "🗓️ Stick to a care calendar — consistency is key for happy plants!",
        "🚫 Avoid overwatering — soggy roots can lead to root rot and disease.",
        "🔄 Rotate indoor plants weekly to ensure even exposure to sunlight.",
        "🌼 Use compost to enrich your soil naturally and improve plant vitality.",
        "👆 Always check soil moisture before the next watering session.",
        "🥚 Add crushed eggshells to your soil to boost calcium and deter slugs.",
        "🌿 Companion planting works! Basil near tomatoes enhances flavor and repels pests.",
        "🍌 Banana peels make a great natural fertilizer — rich in potassium and phosphorus.",
        "📓 Keep a gardening journal to track what works well each season.",
        "🌧️ Collect rainwater in barrels — it’s the best and most natural for your plants.",
        "🌱 Soak seeds overnight before planting to speed up germination.",
        "🌸 Deadhead flowers regularly to encourage new blooms.",
        "🔄 Rotate seasonal crops to avoid depleting the same soil nutrients.",
        "🍅 Prune tomato plants weekly to improve airflow and fruit yield.",
        "🌞 Ensure sun-loving plants get at least 6 hours of direct sunlight daily.",
        "🌿 Snip herbs often — it promotes bushy growth and delays flowering.",
        "👁️ Check leaves frequently — yellowing can mean overwatering or nutrient deficiency.",
        "🪴 Mulching materials like straw, leaves, or bark keep weeds down and moisture in.",
        "💡 Fun fact: Companion planting can improve yields *and* reduce pests naturally!"
    ]


def get_daily_tip():
    idx = datetime.date.today().toordinal() % len(DAILY_TIPS)
    return DAILY_TIPS[idx]






def main():
    # Title
    st.title("🌿 Urban Gardening Helper")
    st.subheader("Find plants suitable for your urban space 🌇")
    
    @st.cache_data
    def load_plants_data():
        file_path = os.path.join("data", "plants_db.json")
        with open(file_path, "r") as file:
            return json.load(file)


    # Show random tip per visit
    st.markdown("### 🧠 Gardening Tip of the Day")
    st.info(get_daily_tip())

    plants_data = load_plants_data()
    # Simulated JSON-style plant database (inline)
    
    # Input fields
    space = st.selectbox("Where do you want to grow?", ["Select", "balcony", "terrace", "window", "community garden"])
    sunlight = st.selectbox("How much sunlight do you get?", ["Select", "full", "partial", "shade"])
    water = st.selectbox("How much water can you provide?", ["Select", "low", "medium", "high"])
    is_beginner = st.checkbox("Show only beginner-friendly plants 🌱")
    max_days = st.slider("Maximum growth time (days)", 20, 180, 90)

    # Show matching plants
    if st.button("Suggest Plants 🌿"):
        if "Select" in [space, sunlight, water]:
            st.warning("Please complete all selections.")
        else:
            matched = []
            for plant in plants_data:
                if (space in plant["space"] and
                    sunlight in plant["sunlight"] and
                    water in plant["water"] and
                    (not is_beginner or plant["beginner_friendly"]) and
                    plant["estimated_growth_days"] <= max_days):
                    matched.append(plant)

            if matched:
                st.success(f"🌿 Found {len(matched)} matching plant(s):")
                for plant in matched:
                    st.image(plant["image"], width=300)
                    st.markdown(f"### {plant['name']}")
                    st.write(f"**Sunlight:** {', '.join(plant['sunlight'])}")
                    st.write(f"**Water Needs:** {', '.join(plant['water'])}")
                    st.write(f"**Beginner Friendly:** {'✅' if plant['beginner_friendly'] else '❌'}")
                    st.write(f"**Est. Growth Time:** {plant['estimated_growth_days']} days")
                    st.write(f"**Uses:** {plant['uses']}")
                    st.write(f"**Care:** {plant['care']}")
                    st.write(f"**Growth Process:** {plant['growth_process']}")
                    st.markdown("---")
            else:
                st.error("No matching plants found for the selected criteria.")


    # ------------------------------------------
    # Harvest Estimator Section
    # ------------------------------------------

    st.header("🌾 Harvest Estimator for Urban Gardening")

    area_type = st.selectbox("Select area type", ["balcony", "garden", "terrace", "community garden"])
    total_space = st.number_input("Enter total available space (in sq. ft)", min_value=10, step=5)
    family_size = st.number_input("Enter family size", min_value=1, step=1)
    growing_method = st.selectbox("Preferred growing method", ["soil", "hydroponic", "vertical"])
    daily_veg_per_person = st.number_input("Vegetable consumption per person per day (grams)", min_value=100, step=50)

    if st.button("Estimate Harvest Plan"):
        total_daily_veg = family_size * daily_veg_per_person  # in grams
        total_monthly_veg = total_daily_veg * 30 / 1000  # in kg

        # Define average yield per sq. ft (very approximate)
        yield_per_sqft = {
            "soil": 0.3,        # kg/month/sq.ft
            "hydroponic": 0.5,  # more efficient
            "vertical": 0.7     # most efficient
        }

        expected_yield = yield_per_sqft[growing_method] * total_space  # kg/month

        st.subheader("🍅 Estimated Output:")
        st.markdown(f"- **Monthly Veg Requirement:** `{total_monthly_veg:.2f} kg`")
        st.markdown(f"- **Estimated Yield (with {growing_method} method):** `{expected_yield:.2f} kg/month`")

        if expected_yield >= total_monthly_veg:
            st.success("✅ You can meet your family's vegetable needs with this setup!")
        else:
            st.error("⚠️ Current setup may not be sufficient. Consider increasing space or trying a vertical/hydroponic method.")