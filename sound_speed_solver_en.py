import streamlit as st
import math

# --- Page config ---
st.set_page_config(page_title="Aguamenti Polluter Calculator", page_icon="💧", layout="centered")

# --- Animated Background CSS ---
page_bg = """
<style>
body {
    margin: 0;
    font-family: 'Segoe UI', sans-serif;
    color: #e0e1dd;
    overflow-x: hidden;
}

/* Animated gradient background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(-45deg, #0b132b, #1c2541, #0b132b, #3a506b);
    background-size: 400% 400%;
    animation: gradientMove 12s ease infinite;
}

@keyframes gradientMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Title */
h1 {
    color: #c5a300;
    text-align: center;
    font-weight: 900;
    text-shadow: 0 0 10px #c5a300;
}

/* Labels */
.stSelectbox label, .stNumberInput label {
    color: #e0e1dd !important;
    font-size: 18px;
    font-weight: 600;
}

/* Input boxes */
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

/* Animated wave effect at bottom */
.wave {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 200%;
    height: 120px;
    background: radial-gradient(circle, #c5a30033 20%, transparent 70%);
    animation: waveMove 6s linear infinite;
    opacity: 0.4;
}
@keyframes waveMove {
    0% { transform: translateX(0); }
    100% { transform: translateX(-50%); }
}
</style>
<div class="wave"></div>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --- Title ---
st.title("💧 Aguamenti Polluter Calculator")

st.markdown(
    "Use this scientific calculator to determine the **number of moles (n)** "
    "and **total mass** of heavy metal pollutants based on the measured speed."
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

