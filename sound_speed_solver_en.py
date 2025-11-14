import streamlit as st
import math

# إعداد الصفحة
st.set_page_config(page_title="Aguamenti Calculator", layout="centered")

# تصميم العنوان
st.markdown("<h1 style='text-align: center; color: #3b5998;'>Aguamenti Calculator for Heavy Metals</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #3b5998; font-size:18px;'>A calculator that gives you the amount of heavy metals in fresh water using the velocity of sound</p>", unsafe_allow_html=True)

st.markdown("---")

# اختيار المعدن
st.markdown("### Choose the metal")
metal = st.selectbox("", ["Lead (Pb)", "Cadmium (Cd)", "Mercury (Hg)"])

# إدخال سرعة الصوت
st.markdown("### Enter the velocity of sound (m/s)")
v_input = st.number_input("", min_value=0.0, format="%.10f")

# القيم المولية للمعدن بالجرام/مول
molar_masses = {"Lead (Pb)": 207.2, "Cadmium (Cd)": 112.41, "Mercury (Hg)": 200.59}

# المعايير للأمان بالملليجرام
safety_limits = {"Lead (Pb)": 0.01, "Cadmium (Cd)": 0.003, "Mercury (Hg)": 0.001}

# ثابت الحساب
constant = 2.2 * 10**9 * 10**-3

# حساب عدد المولات والكتلة
molar_mass = molar_masses[metal]

if v_input <= 0:
    st.error("The velocity entered is invalid. Must be greater than zero.")
else:
    n_calc = (constant / (v_input**2) - 1) / (molar_mass * 10**-3)
    
    if n_calc < 0:
        st.error("Calculated moles is negative. Check your velocity input.")
        n_calc = 0
    
    mass_mg = n_calc * molar_mass * 1000  # بالملليجرام

    # التأكد من تنسيق الأرقام بدون صيغة e
    n_display = f"{n_calc:.10f}"
    mass_display = f"{mass_mg:.10f}"

    # مربعات النتائج
    col1, col2, col3 = st.columns(3)
    
    col1.markdown(f"<div style='background-color:#ADD8E6; padding:15px; border-radius:10px; text-align:center;'>Moles<br>{n_display}</div>", unsafe_allow_html=True)
    col2.markdown(f"<div style='background-color:#ADD8E6; padding:15px; border-radius:10px; text-align:center;'>Mass (mg)<br>{mass_display}</div>", unsafe_allow_html=True)
    
    # مربع الأمان
    if mass_mg > safety_limits[metal]:
        col3.markdown(f"<div style='background-color:#FF6347; padding:15px; border-radius:10px; text-align:center;'>Unsafe for human use</div>", unsafe_allow_html=True)
    else:
        col3.markdown(f"<div style='background-color:#90EE90; padding:15px; border-radius:10px; text-align:center;'>Safe for human use</div>", unsafe_allow_html=True)
    
    # الحد الأقصى للكتلة لكل عنصر
    st.markdown(f"<p style='text-align:center; color:#3b5998;'>Maximum safe mass limits: Lead = 0.01 mg, Cadmium = 0.003 mg, Mercury = 0.001 mg</p>", unsafe_allow_html=True)

