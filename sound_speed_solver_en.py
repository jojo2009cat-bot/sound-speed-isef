import streamlit as st
import math

# --- إعداد الصفحة ---
st.set_page_config(page_title="Aguamenti Calculator for Heavy Metals", layout="centered")
st.markdown("""
    <h1 style='text-align: center; color: #2a3eb1;'>Aguamenti Calculator for Heavy Metals</h1>
    <h4 style='text-align: center; color: #4a4a4a;'>A calculator that gives you the amount of heavy metals in fresh water using the velocity of sound</h4>
""", unsafe_allow_html=True)

st.markdown("---")

# --- اختيار المعدن ---
st.markdown("<h5>Choose the metal:</h5>", unsafe_allow_html=True)
metal = st.selectbox("", ["Lead (Pb)", "Cadmium (Cd)", "Mercury (Hg)"])

# --- إدخال سرعة الصوت ---
st.markdown("<h5>Enter the velocity of sound (m/s):</h5>", unsafe_allow_html=True)
v_input = st.number_input("", min_value=0.0, format="%.5f")

# --- البيانات الأساسية ---
molar_masses = {
    "Lead (Pb)": 207.2,   # g/mol
    "Cadmium (Cd)": 112.41,
    "Mercury (Hg)": 200.59
}

# --- حساب عدد المولات والكتلة ---
def calculate_moles_and_mass(v, metal_name):
    molar_mass = molar_masses[metal_name]  # g/mol
    try:
        n = (2.2e9 * 1e-3 / (v**2) - 1) / (molar_mass * 1e-3)
        if n < 0:
            return None, None, "Error: Moles calculated as negative!"
        mass_mg = n * molar_mass * 1000  # تحويل للملليجرام
        return n, mass_mg, ""
    except Exception as e:
        return None, None, str(e)

if v_input > 0:
    n, mass_mg, error = calculate_moles_and_mass(v_input, metal)
    
    if error:
        st.error(error)
    else:
        # --- مربعات النتائج ---
        col1, col2, col3 = st.columns(3)

        # مربع عدد المولات
        col1.markdown(f"<div style='background-color:#ADD8E6
