import streamlit as st
import math

# إعداد الصفحة
st.set_page_config(page_title="Aguamenti Calculator", layout="centered")

# عنوان الموقع
st.markdown("<h1 style='text-align: center; color: #2C3E50;'>Aguamenti Calculator for Heavy Metals</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #34495E;'>A calculator that gives you the amount of heavy metals in fresh water using the velocity of sound</p>", unsafe_allow_html=True)
st.markdown("---")

# اختيار العنصر
metal = st.selectbox("Choose the metal", ["Lead (Pb)", "Cadmium (Cd)", "Mercury (Hg)"])

# إدخال سرعة الصوت
velocity_input = st.number_input("Enter the velocity of sound (m/s)", min_value=0.0, step=0.01, format="%.6f")

# بيانات العناصر: الكتلة المولية والحد الأقصى للسلامة (mg)
metals_data = {
    "Lead (Pb)": {"molar_mass": 207.2, "limit_mg": 0.01},
    "Cadmium (Cd)": {"molar_mass": 112.41, "limit_mg": 0.003},
    "Mercury (Hg)": {"molar_mass": 200.59, "limit_mg": 0.001},
}

def calculate_moles_and_mass(v, molar_mass):
    """
    إعادة ترتيب القانون لحساب n:
    v = sqrt((2.2e9 * 1e-3) / (n * molar_mass * 1e-3 + 1))
    """
    try:
        n = (2.2e6 / (v**2)) - 1
        n = n / (molar_mass * 1e-3)
        if n < 0:
            return -1, 0
        mass_mg = n * molar_mass * 1000  # تحويل للمللي جرام
        return n, mass_mg
    except:
        return -1, 0

if velocity_input > 0:
    n, mass_mg = calculate_moles_and_mass(velocity_input, metals_data[metal]["molar_mass"])

    if n < 0:
        st.error("The calculated number of moles is negative. Please check the velocity input.")
        n = 0
        mass_mg = 0

    # عرض النتائج
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"<div style='background-color:#ADD8E6; padding:20px; text-align:center; border-radius:10px;'>Moles<br>{n:.6f}</div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div style='background-color:#ADD8E6; padding:20px; text-align:center; border-radius:10px;'>Mass (mg)<br>{mass_mg:.6f}</div>", unsafe_allow_html=True)
    with col3:
        limit = metals_data[metal]["limit_mg"]
        if mass_mg > limit:
            color = "#E74C3C"
            text = "Unsafe for human use"
        else:
            color = "#2ECC71"
            text = "Safe for human use"
        st.markdown(f"<div style='background-color:{color}; padding:20px; text-align:center; border-radius:10px;'>{text}</div>", unsafe_allow_html=True)

    # الحد الأدنى للكتلة لكل عنصر
    st.markdown("---")
    st.markdown(f"Minimum detectable mass (mg) for each element:")
    st.markdown(f"- Lead (Pb): {metals_data['Lead (Pb)']['limit_mg']} mg")
    st.markdown(f"- Cadmium (Cd): {metals_data['Cadmium (Cd)']['limit_mg']} mg")
    st.markdown(f"- Mercury (Hg): {metals_data['Mercury (Hg)']['limit_mg']} mg")

else:
    st.warning("Please enter a velocity greater than zero to calculate.")

