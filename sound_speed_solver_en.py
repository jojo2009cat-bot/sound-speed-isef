import streamlit as st
import math

# --- Page config ---
st.set_page_config(page_title="ISEF Chemical System", page_icon="🔬", layout="centered")

# --- Custom background and styling ---
page_bg = """
<style>
body {
    background: linear-gradient(135deg, #0b132b 40%, #1c2541 80%);
    color: #e0e1dd;
    font-family: 'Segoe UI', sans-serif;
}

[data-testid="stAppViewContainer"] {
    background-image: radial-gradient(circle at 10% 20%, #0b132b, #1c2541, #0b132b);
    background-attachment: fixed;
}

h1 {
    color: #c5a300;
    text-align: center;
    font-weight: 900;
    text-shadow: 1px 1px 4px #888;
}

.stSelectbox label, .stNumberInput label {
    color: #e0e1dd !important;
    font-size: 18px;
    font-weight: 600;
}

.stNumberInput input {
    background-color: #1c2541 !important;
    color: white !important;
    border: 1px solid #c5a300 !important;
    border-radius: 8px;
}

.stButton>button {
    background-color: #c5a300 !important;
    color: black !important;
    border: none;
    font-size: 18px;
    font-weight: bold;
    border-radius: 10px;
    padding: 0.6em 1.2em;
    transition: 0.3s;
}

.stButton>button:hover {
    background-color: #e0c94d !important;
    transform: scale(1.05);
}

.result-box {
    background-color: rgba(197, 163, 0, 0.9);
    color: #000;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    font-size: 20px;
    font-weight: bold;
    margin-top: 10px;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --- Title ---
st.title("🔬 ISEF Chemical System Calculator")

st.markdown(
    "Use this calculator to find the **number of moles (n)** and **total mass** from a given speed value."
)

# --- Element selection ---
element = st.selectbox(
    "Select the element:",
    ["Cadmium (Cd)", "Mercury (Hg)", "Lead (Pb)"]
)

# --- User input ---
result = st.number_input("Enter the calculated speed:", min_value=0.0, format="%.4f")

# --- Constants ---
B = 2.2 * 10**9  # Bulk modulus (Pa)
density = 1 / (10**3)  # density factor (kg/m³)
molar_masses = {
    "Cadmium (Cd)": 112.4,
    "Mercury (Hg)": 200.59,
    "Lead (Pb)": 207.2
}

# --- Calculation ---
if st.button("Calculate"):
    M = molar_masses[element]
    try:
        n = ((math.sqrt(B * density) / result) - 1) / (M * (1 / 10**3))
        if n < 0:
            st.error("❌ Invalid result: the number of moles cannot be negative.")
        else:
            total_mass = n * M
            st.markdown(f"<div class='result-box'>Number of moles (n): {n:.4f}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='result-box'>Total mass: {total_mass:.4f} g</div>", unsafe_allow_html=True)
    except Exception as e:
        st.error(f"⚠️ Calculation error: {e}")
