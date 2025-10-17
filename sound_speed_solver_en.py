import streamlit as st
import math

# --- Page config ---
st.set_page_config(page_title="Aguamenti Polluter Calculator", page_icon="🌊", layout="centered")

# --- Custom animated background and style ---
page_bg = """
<style>
body {
    margin: 0;
    font-family: 'Segoe UI', sans-serif;
    color: #e0e1dd;
    overflow-x: hidden;
}

/* Background gradient animation */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0b132b, #1c2541, #c5a300, #0b132b);
    background-size: 400% 400%;
    animation: bgmove 12s ease infinite;
}

@keyframes bgmove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Main Title */
h1 {
    text-align: center;
    font-size: 50px !important;
    font-weight: 900 !important;
    background: linear-gradient(90deg, #c5a300, #e0c94d, #c5a300);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0px 0px 10px rgba(197, 163, 0, 0.4);
    letter-spacing: 1.5px;
}

/* Description text */
.stMarkdown {
    text-align: center;
    font-size: 17px;
    color: #f1f1f1;
}

/* Inputs and labels */
.stSelectbox label, .stNumberInput label {
    color: #e0e1dd !important;
    font-size: 18px;
    font-weight: 600;
}
.stNumberInput input {
    background-color: rgba(255,255,255,0.1) !important;
    color: white !important;
    border: 1px solid #c5a300 !important;
    border-radius: 8px;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #c5a300, #e0c94d);
    color: #000;
    border: none;
    font-size: 18px;
    font-weight: bold;
    border-radius: 10px;
    padding: 0.6em 1.2em;
    transition: all 0.4s ease;
    box-shadow: 0 0 10px rgba(197,163,0,0.6);
}
.stButton>button:hover {
    background: linear-gradient(90deg, #e0c94d, #c5a300);
    transform: scale(1.07);
}

/* Result box */
.result-box {
    background: rgba(197, 163, 0, 0.9);
    color: #000;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    font-size: 20px;
    font-weight: bold;
    margin-top: 10px;
    box-shadow: 0 0 10px rgba(197,163,0,0.6);
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --- Title ---
st.title("Aguamenti Polluter Calculator")

# --- Description (from the ISEF version) ---
st.markdown(
    "Use this calculator to find the **number of moles (n)** and **total mass** "
    "of heavy metal pollutants based on the calculated speed in your experiment."
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

