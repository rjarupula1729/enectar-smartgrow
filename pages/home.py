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
        🌱 **Empowering you to grow your own food – no matter where you live!**  
        This platform is designed to help urban dwellers cultivate vegetables and herbs based on their available space, time, and environmental conditions.

        ### ✨ Key Features:
        - 🧮 **Estimate Costs & Yields:** Plan your harvest with our smart cost calculator  
        - 🛒 **Get What You Need:** Shop seeds, tools, and kits curated for your setup  
        - 🎮 **Learn & Play:** Gamified learning and interactive guides to make gardening fun  
        - 📊 **Monitor Growth:** Track plant progress and get personalized care tips  

        👉 Use the sidebar to navigate through the features and start your gardening journey!
    """)
  #  st.title("🌿 Why this App?")
    st.markdown("""
        ## 🌿 Why this App ?

            **Grow fresh, organic veggies right from your balcony, terrace, or backyard!**  
            We're on a mission to bring healthy, pesticide-free food closer to your plate — by helping you grow it yourself.

            ✅ Cut down grocery expenses  
            ✅ Improve your health naturally  
            ✅ Contribute to a greener, cleaner world 🌍  
        """)

elif selection == "🌱 Plant Recommendation":
    from pages import recommendations
    recommendations.main()

elif selection == "📋 Plant Tracker":
    from pages import plant_tracker
    plant_tracker.main()

#elif selection == "🌾 Harvest Estimator":
#    import harvest_estimator
#    harvest_estimator.main()

elif selection == "💰 Cost Estimator":
    from pages import price_model
    price_model.main()

elif selection == "🛒 Shop & Cart":
    from pages import shop_cart
    shop_cart.main()

elif selection == "🎮 Games / Entertainment / Knowledge Check":
    from pages import game_zone
    game_zone.main()

elif selection == "🤝 Expert Support & Monetization":
    from pages import growpal_connect
    growpal_connect.main()
