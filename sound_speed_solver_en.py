import streamlit as st
import math

# --- إعداد الصفحة ---
st.set_page_config(page_title="Aguamenti Calculator for Heavy Metals", layout="centered")
st.markdown("""
    <style>
        body {
            background: linear-gradient(to bottom, #fff9c4, #bbdefb);
            font-family: 'Arial', sans-serif;
        }
        .title {
            text-align: center;
            font-size: 32px;
            font-weight: bold;
            margin-bottom: -10px;
        }
        .subtitle {
            text-align: center;
            font-size: 18px;
            margin-bottom: 30px;
        }
        .result-box {
            background-color: #b3e5fc;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            font-size: 20px;
            margin-bottom: 15px;
        }
        .safe {
            background-color: #c8e6c9;
            color: black;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            font-size: 20px;
            margin-bottom: 15px;
        }
        .unsafe {
            background-color: #f8bbd0;
            color: black;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            font-size: 20px;
            margin-bottom: 15px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">Aguamenti Calculator for Heavy Metals</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">A calculator that gives you the amount of heavy metals in fresh water using the velocity of sound</div>', unsafe_allow_html=True)

# --- اختيار العنصر ---
st.markdown("**Choose the metal:**")
metal = st.selectbox("", ["Lead (Pb)", "Cadmium (Cd)", "Mercury (Hg)"])

# --- إدخال سرعة الصوت ---
st.markdown("**Enter the velocity of sound (m/s):**")
velocity_input = st.text_input("", value="0.0")

# --- تعريف بيانات المعادن ---
metal_data = {
    "Lead (Pb)": {"molar_mass": 207.2, "limit_mg": 0.01},
    "Cadmium (Cd)": {"molar_mass": 112.41, "limit_mg": 0.003},
    "Mercury (Hg)": {"molar_mass": 200.59, "limit_mg": 0.001}
}

try:
    v = float(velocity_input)
    if v <= 0:
        st.error("Error: velocity must be positive")
    else:
        M = metal_data[metal]["molar_mass"]
        limit = metal_data[metal]["limit_mg"]

        # حساب عدد المولات
        n = 2.2e6 / ((v**2 * 1) - 1) / M  # معادلة عكسية للـv
        if n < 0:
            st.error("Error: calculated moles is negative")
            n = 0
        # حساب الكتلة بالملليجرام
        mass_mg = n * M
        if mass_mg < 0:
            mass_mg = 0

        # --- عرض النتائج ---
        st.markdown(f'<div class="result-box">Number of moles: {round(n, 8)}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="result-box">Mass (mg): {round(mass_mg, 8)}</div>', unsafe_allow_html=True)

        # مربع safe/unsafe
        if mass_mg > limit:
            st.markdown(f'<div class="unsafe">Unsafe for human use</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="safe">Safe for human use</div>', unsafe_allow_html=True)

        # الحد الأقصى لكل معدن
        st.markdown(f"Maximum allowed mass for {metal}: {limit} mg")

except ValueError:
    st.error("Please enter a valid number for velocity")

