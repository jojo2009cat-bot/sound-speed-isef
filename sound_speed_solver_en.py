import streamlit as st
import math

# === Page configuration ===
st.set_page_config(page_title="Aguamenti Polluter Calculator", layout="centered")

# === Custom CSS for style ===
st.markdown("""
<style>
body {
    background-color: #001F3F; /* Dark blue background */
    color: #F5F5F5;
    border: 6px solid #DAA520; /* Gold border */
    border-radius: 20px;
    padding: 20px;
}

h1 {
    color: #FFD700;
    font-family: 'Trebuchet MS', sans-serif;
    text-align: center;
    font-size: 46px;
    letter-spacing: 2px;
    text-shadow: 0px 0px 15px #FFD700;
    margin-bottom: 10px;
}

div[data-testid="stAppViewContainer"] {
    background-color: #001F3F; /* Keep background dark blue */
    border-radius: 20px;
    padding: 25px;
}

div[data-testid="stMarkdownContainer"] {
    font-size: 18px;
    color: #E0E0E0;
    text-align: center;
}

.stButton>button {
    background-color: #DAA520;
    color: black;
    border-radius: 12px;
    font-size: 18px;
    font-weight: bold;
    transition: 0.3s;
}
.stButton>button:hover {
    background-color: #FFD700;
    color: #001F3F;
}
</style>
""", unsafe_allow_html=True)

# === App Title ===
st.title("🌊 Aguamenti Polluter Calculator")

# === Description (restored to your favorite version) ===
st.markdown("""
Welcome to the **Aguamenti Polluter Calculator** —  
a specialized system designed to **analyze pollutant behavior** in water  
by calculating the **molar quantity and total mass** based on the measured sound speed.  
Perfect for **ISEF research projects** focused on heavy metals and environmental pollution.
""")

# === Element selection ===
element = st.selectbox(
    "Select the element:",
    ["Cadmium (Cd)", "Mercury (Hg)", "Lead (Pb)"]
)

# Assign molar masses
molar_masses = {
    "Cadmium (Cd)": 112.4,
    "Mercury (Hg)": 200.59,
    "Lead (Pb)": 207.2
}
molar_mass = molar_masses[element]

# === Input field for speed ===
speed = st.number_input("Enter the calculated speed (m/s):", min_value=0.0, step=0.1)

# === Calculation button ===
if st.button("Calculate"):
    bulk_modulus = 2.2e9
    density_water = 1000  # kg/m³

    try:
        # Derived formula for n
        numerator = (bulk_modulus / (speed ** 2)) * (1 / density_water) - 1
        n = numerator / (molar_mass * (1 / density_water))

        if n < 0 or math.isnan(n):
            st.error("❌ Invalid result: The calculated number of moles is negative or undefined. Please check your inputs.")
        else:
            total_mass = n * molar_mass
            st.success(f"✅ Number of moles (n): **{n:.4f} mol**")
            st.info(f"💡 Total mass: **{total_mass:.4f} g**")
    except ZeroDivisionError:
        st.error("Speed cannot be zero.")

