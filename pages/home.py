import streamlit as st

# Page title
st.set_page_config(page_title="Smart Urban Gardening App", layout="wide")

# Sidebar Navigation
st.sidebar.title("🌿 Smart Gardening Menu")
selection = st.sidebar.radio("Go to", [
    "🏡 Home",
    "🌱 Plant Recommendation",
    "📋 Plant Tracker",
  #  "🌾 Harvest Estimator",
    "💰 Cost Estimator",
    "🛒 Shop & Cart",
    "🎮 Games / Entertainment / Knowledge Check",
    "🤝 Expert Support & Monetization"
])

# Page Routing
if selection == "🏡 Home":
    st.title("🏡 Welcome to Smart Urban Gardening Platform")
    st.markdown("""
        This app helps urban users:
        - Grow their own vegetables 🍅🌿
        - Estimate harvest & cost 💸
        - Shop required materials 🛍️
        - Play, learn & earn with gardening 🎉

        Use the sidebar to navigate through different tools.
    """)

elif selection == "🌱 Plant Recommendation":
    import recommendations
    recommendations.main()

elif selection == "📋 Plant Tracker":
    import plant_tracker
    plant_tracker.main()

#elif selection == "🌾 Harvest Estimator":
#    import harvest_estimator
#    harvest_estimator.main()

elif selection == "💰 Cost Estimator":
    import price_model
    price_model.main()

elif selection == "🛒 Shop & Cart":
    import shop_cart
    shop_cart.main()

elif selection == "🎮 Games / Entertainment / Knowledge Check":
    import game_zone
    game_zone.main()

elif selection == "🤝 Expert Support & Monetization":
    import growpal_connect
    growpal_connect.main()
