import streamlit as st



# Define shop items
shop_items = {
    "Seeds": {"Tomato Seeds (50g)": 50, "Spinach Seeds (50g)": 30, "Coriander Seeds (30g)": 20},
    "Saplings": {"Tomato Sapling": 15, "Chili Sapling": 20, "Brinjal Sapling": 25},
    "Compost": {"Organic Compost (5kg)": 100, "Cocopeat (2kg)": 60},
    "Hydroponic Accessories": {"Net Pots (Set of 10)": 100, "Nutrient Solution (1L)": 200, "pH Testing Kit": 150},
    "Beginner Kits": {"Soil Grow Kit": 500, "Hydroponic Starter Kit": 1200}
}

#st.set_page_config(page_title="Nector Garden Store", layout="centered")

st.title("🛒 Gardening Shop – Add to Cart & Checkout")
st.markdown("Browse and purchase essentials for your garden!")

cart = {}

# Shopping UI
for category, items in shop_items.items():
    st.subheader(f"🧺 {category}")
    for item_name, price in items.items():
        col1, col2, col3 = st.columns([4, 1, 2])
        with col1:
            st.write(f"{item_name}")
        with col2:
            st.write(f"₹{price}")
        with col3:
            qty = st.number_input(f"Qty for {item_name}", min_value=0, max_value=10, step=1, key=item_name)
            if qty > 0:
                cart[item_name] = {"price": price, "quantity": qty}

st.markdown("---")
st.subheader("🧾 Cart Summary")

if cart:
    total = 0
    for item, info in cart.items():
        item_total = info["price"] * info["quantity"]
        total += item_total
        st.write(f"- {item} × {info['quantity']} = ₹{item_total}")
    
    st.markdown(f"### 🧮 **Total Bill: ₹{total}**")

    if st.button("🛍️ Proceed to Pay"):
        st.success("✅ Payment Successful (Mock). Thank you for shopping with Nector Garden!")
else:
    st.info("Your cart is empty. Add items to proceed.")

