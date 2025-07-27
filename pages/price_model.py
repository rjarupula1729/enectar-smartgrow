import streamlit as st

def main(): 
    # Price estimation constants (customize as needed)
    PRICE_PER_SQFT = {
        "soil": 100,
        "hydroponic": 250,
        "vertical": 400
    }

    COMMUNITY_SUPPORT_COST = 15000  # Optional base cost for community support setup

    st.title("🌱 Community Growth Model Estimator")

    st.markdown("""
    Estimate the setup cost for growing your own vegetables in a community or urban setup using various methods like soil, hydroponics, or vertical farming.
    """)

    # Input form
    with st.form("community_growth_form"):
        area_type = st.selectbox("Select Area Type", ["balcony", "garden", "terrace", "community garden"])
        available_space = st.number_input("Enter Total Available Space (in sq. ft)", min_value=10, step=10)
        family_size = st.number_input("Enter Family Size", min_value=1, step=1)
        method = st.selectbox("Select Growing Method", ["soil", "hydroponic", "vertical"])
        support_required = st.checkbox("Include Community Growth Support?")
        submitted = st.form_submit_button("Estimate Cost")

    if submitted:
        # Cost estimation
        base_cost = available_space * PRICE_PER_SQFT[method]
        total_cost = base_cost + (COMMUNITY_SUPPORT_COST if support_required else 0)

        st.success("✅ Estimated Setup Cost")
        st.markdown(f"**Selected Area Type:** {area_type}")
        st.markdown(f"**Growing Method:** {method.title()}")
        st.markdown(f"**Total Space:** {available_space} sq.ft")
        st.markdown(f"**Family Size:** {family_size}")
        st.markdown(f"**Support Required:** {'Yes' if support_required else 'No'}")
        st.markdown("---")
        st.markdown(f"### 💰 Total Estimated Cost: ₹{total_cost:,}/-")
        st.markdown("""
        _Note: Actual costs may vary depending on local pricing and additional factors such as automation, water systems, and pest control._
        """)
