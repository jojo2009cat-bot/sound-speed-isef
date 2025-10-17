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
st.title("Aguamenti Polluter Calculator")

# === Description ===
st.markdown("""
Welcome to the **Aguamenti Polluter Calculator** 🌊  
This tool helps you estimate pollutant molar quantity and total mass  
based on the measured sound speed in a solution.
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
molar_ma_
