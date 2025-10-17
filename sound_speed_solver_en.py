import streamlit as st
import math
from PIL import Image
import base64
from io import BytesIO

# === إعداد صفحة التطبيق مع أيقونة الموجة في التاب ===
# سننشئ أيقونة موجة ذهبية صغيرة باستخدام SVG ونحولها لصورة PNG
import io
import cairosvg

wave_svg = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<path d="M2 40c5-8 10-8 15 0s10 8 15 0 10-8 15 0 10 8 15 0" stroke="#FFD700" stroke-width="4" fill="none"/>
</svg>
"""
png_bytes = cairosvg.svg2png(bytestring=wave_svg.encode('utf-8'))
wave_icon = Image.open(io.BytesIO(png_bytes))

st.set_page_config(
    page_title="Aguamenti Polluter Calculator",
    page_icon=wave_icon,
    layout="centered"
)

# === Custom CSS for elegant design ===
st.markdown("""
<style>
body {
    background-color: #001F3F; /* Dark blue */
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
    background-color: #001F3F;
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

# === Description (new version) ===
st.markdown("""
Welcome to **Aguamenti Polluter Calculator**.  
Use this calculator to determine the **number of moles (n)** and the **total mass**  
of the heavy metal you choose, using the **calculated sound speed** in your experiment.
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

