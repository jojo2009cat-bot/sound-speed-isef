import streamlit as st
import math

# --- Styling ---
st.markdown("""
    <style>
    body {
        background-color: #0b132b;
        color: #e0e1dd;
    }
    .stSelectbox, .stNumberInput, .stButton {
        background-color: #1c2541 !important;
        color: #ffffff !important;
    }
    .result-box {
        background-color: #c5a300;
        color: #000;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- App Title ---
st.title("🔬 ISEF Chemical System Calculator")
st.markdown("This system calculates the **number of moles (n)** and **total mass** based on the given result.")

# --- Element selection ---
element = st.selectbox(
    "Select the element:",
    ["Cadmium (Cd)", "Mercury (Hg)", "Lead (Pb)"]
)

# --- User input ---
result = st.number_input("Enter the measured result:", min_value=0.0, format="%.4f")

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
    
    # Rearranged formula to find n:
    # result = sqrt(2.2×10⁹×1/10³) ÷ ((n×M×1/10³) + 1)
    # => n = ((sqrt(2.2×10⁹×1/10³) / result) - 1) / (M×1/10³)
    
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

