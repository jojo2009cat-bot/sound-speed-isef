import streamlit as st
import math

# Constants
CONSTANT = 2.2e6  # 2.2 * 10^9 * 10^-3
MOLAR_MASSES = {
    "Lead (Pb)": 207.2,
    "Cadmium (Cd)": 112.41,
    "Mercury (Hg)": 200.59
}
THRESHOLDS = {
    "Lead (Pb)": 0.01,
    "Cadmium (Cd)": 0.003,
    "Mercury (Hg)": 0.001
}

# Function to calculate n from v
def calculate_n(v, M):
    if v <= 0:
        return None  # Invalid velocity
    denominator = CONSTANT / (v ** 2)
    if denominator <= 1:
        return None  # Would make n negative
    n = (denominator - 1) / (M * 0.001)
    return n if n >= 0 else None

# Function to calculate mass in mg
def calculate_mass(n, M):
    return n * M * 1000 if n is not None else None

# Streamlit app
st.set_page_config(page_title="Aguamenti Calculator for Heavy Metals", page_icon="🧪", layout="centered")

# Custom CSS for dark sky blue background and soft colors
st.markdown("""
<style>
    body {
        background-color: #4682b4;  /* Steel blue, dark sky blue */
        color: #fff;
    }
    .stApp {
        background-color: #4682b4;
    }
    .title {
        color: #f0f8ff;  /* Light blue for contrast */
        font-size: 2.5em;
        text-align: center;
    }
    .subtitle {
        color: #daa520;  /* Goldenrod, light yellow */
        font-size: 1.2em;
        text-align: center;
        margin-bottom: 20px;
    }
    .result-box {
        background-color: #add8e6;  /* Light blue */
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
        text-align: center;
        font-weight: bold;
        color: #000;
    }
    .safe {
        background-color: #90ee90;  /* Light green */
        color: #006400;
    }
    .unsafe {
        background-color: #ff6347;  /* Tomato red */
        color: #8b0000;
    }
    .safety-note {
        font-size: 0.9em;
        color: #f0f8ff;
        text-align: center;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="title">Aguamenti Calculator for Heavy Metals</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">A calculator that gives you the amount of heavy metals in fresh water using the velocity of sound</p>', unsafe_allow_html=True)

# Input section
st.subheader("Inputs")
metal = st.selectbox("Choose the metal", list(MOLAR_MASSES.keys()))
velocity = st.number_input("Enter the velocity of sound (m/s)", min_value=0.0, step=0.01, format="%.6f")

# Calculate button
if st.button("Calculate"):
    M = MOLAR_MASSES[metal]
    threshold = THRESHOLDS[metal]
    
    n = calculate_n(velocity, M)
    if n is None:
        st.error("Error: The number of moles came out negative. Please check the velocity input.")
    else:
        mass_mg = calculate_mass(n, M)
        
        # Display results
        st.subheader("Results")
        
        # Number of moles
        st.markdown(f'<div class="result-box">Number of moles: {n:.10f}</div>', unsafe_allow_html=True)
        
        # Mass in mg/L
        st.markdown(f'<div class="result-box">Mass in mg/L: {mass_mg:.10f}</div>', unsafe_allow_html=True)
        
        # Safety check
        if mass_mg > threshold:
            safety_class = "unsafe"
            safety_text = "Unsafe for human use"
        else:
            safety_class = "safe"
            safety_text = "Safe for human use"
        
        st.markdown(f'<div class="result-box {safety_class}">{safety_text}</div>', unsafe_allow_html=True)
        
        # Maximum threshold
        st.write(f"Maximum safe mass for {metal}: {threshold} mg/L")

# Safety criteria note
st.markdown("""
<div class="safety-note">
    <strong>Safety Criteria:</strong> The thresholds used are based on Egyptian standards for drinking water quality. For Lead (Pb), the maximum allowable limit is 0.01 mg/L; for Cadmium (Cd), it is 0.003 mg/L; and for Mercury (Hg), it is 0.001 mg/L. Concentrations exceeding these limits are considered unsafe for human consumption.
</div>
""", unsafe_allow_html=True)

