import streamlit as st
import random
from datetime import date

# Title
st.title("🌿 Urban Gardening Helper")
st.subheader("Find plants suitable for your urban space 🌇")

# Gardening Tips
gardening_tips = [
    "🌱 Water early in the morning to reduce evaporation.",
    "🌿 Prune dead leaves regularly for healthy growth.",
    "☀️ Give plants enough sunlight, but avoid midday heat.",
    "🐛 Watch out for pests – neem oil works great!",
    "🍃 Mulch helps retain soil moisture and reduce weeds.",
    "📅 Create a care calendar – consistency is key!",
    "🚿 Don’t overwater – soggy roots are harmful!",
    "🪴 Rotate indoor plants weekly for even growth.",
    "🌼 Use compost to enrich your soil naturally.",
    "🔍 Check soil moisture before watering again."
]

# Show random tip per visit
st.markdown("### 🌻 Gardening Tip")
st.success(random.choice(gardening_tips))

# Simulated JSON-style plant database (inline)
plants_data = [
    {
        "name": "Tulsi (Holy Basil)",
        "space": ["balcony", "window", "terrace"],
        "sunlight": ["partial", "full"],
        "water": ["low", "medium"],
        "image": "https://media.gettyimages.com/id/1359257193/photo/lush-green-aromatic-holy-basil-plant-looking-magnificent-ocimum-tenuiflorum-lamiaceae-family.jpg?s=1024x1024&w=gi&k=20&c=Oi-lKtpWM_QqLP1-8C8BaxUJPohjkMktZjBRKk62EvM=",
        "care": "Water twice a week. Needs sunlight 3-4 hrs/day.",
        "uses": "Boosts immunity, reduces stress, supports respiratory health.",
        "growth_process": "Germinate seeds indoors, transplant after 4 weeks, water every alternate day, prune regularly to promote bushy growth.",
        "beginner_friendly": True,
        "estimated_growth_days": 60,
        "season": "Spring to Summer",
        "space_per_plant_sqft": 1.5,
    "yield_per_plant_per_cycle_grams": 150
    },
    {
    "name": "Okra (Lady Finger)",
    "space": ["garden", "community garden"],
    "sunlight": ["full"],
    "water": ["medium"],
    "image": "https://media.gettyimages.com/id/2167011248/photo/okra-and-blossom-flower-growing-in-a-garden.jpg?s=1024x1024&w=gi&k=20&c=TyPPA_4-P8twikUIpYY7BEY3mNg7JNldqzfNqdDy-R8=",   
    "uses": "Good for diabetes, digestion",
    "family_size": 4,
    "growth_process": "Harvest in 50-60 days",
    "care": "Harvest frequently",
    "beginner_friendly": True,
    "space_per_plant_sqft": 1.5,
    "yield_per_plant_per_cycle_grams": 150
    },
    {
        "name": "Coriander",
        "space": ["balcony", "terrace", "window"],
        "sunlight": ["partial"],
        "water": ["medium"],
        "image": "https://media.gettyimages.com/id/1264427026/photo/growing-parsley-in-the-garden.jpg?s=1024x1024&w=gi&k=20&c=bAH7eFAQpOQZy5FXcUZiUB6Ifzc3avvv-V4Nk28r5W4=",
        "care": "Grows fast. Harvest leaves regularly.",
        "uses": "Rich in antioxidants, lowers blood sugar, good for skin.",
        "growth_process": "Sow seeds directly in soil, keep moist till germination, thin seedlings, harvest leaves after 3–4 weeks.",
        "beginner_friendly": True,
        "estimated_growth_days": 30,
        "season": "Winter to Spring",
        "space_per_plant_sqft": 1.5,
    "yield_per_plant_per_cycle_grams": 150
    },
    {
        "name": "Mint (Pudina)",
        "space": ["balcony", "window", "terrace"],
        "sunlight": ["partial", "shade"],
        "water": ["medium", "high"],
        "image": "https://media.gettyimages.com/id/1216984727/photo/fresh-mint-plant-ayurveda-herb-organic.jpg?s=1024x1024&w=gi&k=20&c=n3pRwE6JoR_OuyWajGZhAdFf1PGedmRgGtx2UYrhUh0=",
        "care": "Water regularly. Pinch tops to grow more leaves.",
        "uses": "Aids digestion, freshens breath, soothes headaches.",
        "growth_process": "Plant stem cuttings in moist soil, keep soil damp, trim often to prevent overgrowth and encourage new shoots.",
        "beginner_friendly": True,
        "estimated_growth_days": 40,
        "season": "Spring to Summer",
        "space_per_plant_sqft": 1.5,
    "yield_per_plant_per_cycle_grams": 150
    },
    {
        "name": "Tomato",
        "space": ["terrace", "balcony"],
        "sunlight": ["full"],
        "water": ["high"],
        "image": "https://media.gettyimages.com/id/171579643/photo/tomato-greenhouse.jpg?s=1024x1024&w=gi&k=20&c=TUr8artCrHjk5XzhuVJJ-USZwG9jljF8wsnEWjtJ4oQ=",
        "care": "Needs daily watering. Support plant with stick.",
        "uses": "Rich in Vitamin C, heart-healthy, improves skin health.",
        "growth_process": "Start seeds indoors 6-8 weeks before last frost, transplant outdoors in full sun, water regularly, support with stakes or cages, harvest when fruits are firm and red.",
        "beginner_friendly": False,
        "estimated_growth_days": 90,
        "season": "Summer",
        "space_per_plant_sqft": 1.5,
    "yield_per_plant_per_cycle_grams": 150
    },
    {
        "name": "Aloe Vera",
        "space": ["balcony", "window"],
        "sunlight": ["full", "partial"],
        "water": ["low"],
        "image": "https://media.gettyimages.com/id/182784203/photo/aloe-vera-plant.jpg?s=1024x1024&w=gi&k=20&c=G6kbUDlYoHnKT-tURnC-5cYL6bkJBd5xA6dpOkTpM40=",
        "care": "Very low maintenance. Water weekly.",
        "uses": "Soothes skin, supports digestion, improves oral health.",
        "growth_process": "Use pups from mother plant, plant in sandy soil, water once a week, avoid overwatering to prevent root rot.",
        "beginner_friendly": True,
        "estimated_growth_days": 75,
        "season": "All Seasons",
        "space_per_plant_sqft": 1.5,
    "yield_per_plant_per_cycle_grams": 150
    },
    {
        "name": "Spinach",
        "space": ["terrace", "balcony"],
        "sunlight": ["partial"],
        "water": ["medium"],
        "image": "https://media.gettyimages.com/id/169983791/photo/spinach.jpg?s=1024x1024&w=gi&k=20&c=FMh28QJl8meUK-1VKwQGa5RpjsIovUzy6amDZmypPzA=",
        "care": "Harvest in 30 days. Water every 2-3 days.",
        "uses": "Rich in iron, improves eyesight, boosts energy.",
        "growth_process": "Sow seeds directly in cool weather, keep soil moist, thin seedlings after sprouting, harvest outer leaves regularly to encourage new growth.",
        "beginner_friendly": True,
        "estimated_growth_days": 30,
        "season": "Winter to Spring",
        "space_per_plant_sqft": 1.5,
    "yield_per_plant_per_cycle_grams": 150
    },
    {
        "name": "Chili Plant",
        "space": ["terrace", "balcony"],
        "sunlight": ["full"],
        "water": ["medium"],
        "image": "https://media.gettyimages.com/id/154276389/photo/red-green-peppers.jpg?s=1024x1024&w=gi&k=20&c=hgbR1owIXqTNoviiA-EwSr3pW4Kap74ya-y-37o5ssU=",
        "care": "Fertilize monthly. Keep in sunlight.",
        "uses": "Not Available",
        "growth_process": "Start seeds indoors or directly in warm soil, transplant when 4–6 inches tall, water consistently, provide full sun, harvest when chilies turn bright red or green depending on variety.",
        "beginner_friendly": False,
        "estimated_growth_days": 80,
        "season": "Summer",
        "space_per_plant_sqft": 1.5,
    "yield_per_plant_per_cycle_grams": 150
    },
    {
        "name": "Lemongrass",
        "space": ["terrace"],
        "sunlight": ["full"],
        "water": ["medium", "high"],
        "image": "https://media.gettyimages.com/id/2161967118/photo/lemongrass.jpg?s=1024x1024&w=gi&k=20&c=ntAwP5Zg0JJ4sCQ-blrd91rXw1qZ3VDHjlEe0Vek0x8=",
        "care": "Harvest leaves. Grows tall, so needs big pot.",
        "uses": "Relieves anxiety, boosts immunity, detoxifies the body.",
        "growth_process": "Plant stalks in well-draining soil with full sunlight, keep soil moist until roots develop, divide clumps annually, harvest by cutting mature stalks at the base.",
        "beginner_friendly": True,
        "estimated_growth_days": 100,
        "season": "Spring to Autumn",
        "space_per_plant_sqft": 1.5,
    "yield_per_plant_per_cycle_grams": 150
    },
    {
        "name": "Curry Leaves (Kadi Patta)",
        "space": ["terrace", "balcony"],
        "sunlight": ["full"],
        "water": ["medium"],
        "image": "https://media.gettyimages.com/id/1150140818/photo/curry-leaf-plant.jpg?s=1024x1024&w=gi&k=20&c=KFPSY-Dk686ho8NrSBg7yxPvliznuUnyBaavATbQWxU=",
        "care": "Needs sunlight. Prune regularly.",
        "uses": "Good for eyesight, supports hair growth, anti-inflammatory.",
        "growth_process": "Grow from seeds or stem cuttings, place in sunny area, water moderately, pinch top leaves to promote bushy growth, harvest regularly after plant matures (1–2 years).",
        "beginner_friendly": False,
        "estimated_growth_days": 120,
        "season": "Summer to Autumn",
        "space_per_plant_sqft": 1.5,
    "yield_per_plant_per_cycle_grams": 150
    },
    {
        "name": "Ginger",
        "space": ["balcony", "terrace"],
        "sunlight": ["partial"],
        "water": ["medium", "high"],
        "image": "https://media.gettyimages.com/id/128112512/photo/pile-of-ginger-root-on-green-placemat.jpg?s=1024x1024&w=gi&k=20&c=Lxbo7S7XuaGmfz0e3ECPDbeBB1_NzTFvuIP8qp9mXIE=",
        "care": "Use grow bag. Keep soil moist.",
        "uses": "Ginger is a fragrant kitchen spice.",
        "growth_process": "Plant ginger rhizomes in moist, well-drained soil with indirect sunlight, cover lightly with soil, water gently, shoots appear in 2–3 weeks, harvest after 8–10 months when leaves yellow.",
        "beginner_friendly": False,
        "estimated_growth_days": 150,
        "season": "Spring to Autumn",
        "space_per_plant_sqft": 1.5,
    "yield_per_plant_per_cycle_grams": 150
    }
]

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
