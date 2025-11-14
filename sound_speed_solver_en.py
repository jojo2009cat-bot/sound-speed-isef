import streamlit as st
import math

# --- إعداد الصفحة ---
st.set_page_config(page_title="Aguamenti Calculator for Heavy Metals", layout="centered")
st.markdown("""
    <h2 style='text-align: center; color: #2a3eb1; font-size:28px;'>Aguamenti Calculator for Heavy Metals</h2>
    <h5 style='text-align: center; color: #4a4a4a; font-size:16px;'>A calculator that gives you the amount of heavy metals in fresh water using the velocity of sound</h5>
""", unsafe_allow_html=True)

st.markdown("---")

# --- اختيار المعدن ---
st.markdown("<h6 style='font-size:14px;'>Choose the metal:</h6>", unsafe_allow_html=True)
metal = st.selectbox("", ["Lead (Pb)", "Cadmium (Cd)", "Mercury (Hg)"])

# --- إدخال سرعة الصوت ---
st.markdown("<h6 style='font-size:14px;'>Enter the velocity of sound (m/s):</h6>", unsafe_allow_html=True)
v_input = st.number_input("", min_value=0.0, format="%.5f")

# --- البيانات الأساسية ---
molar_masses = {
    "Lead (Pb)": 207.2,   # g/mol
    "Cadmium (Cd)": 112.41,
    "Mercury (Hg)": 200.59
}

densities = {  # g/cm³
    "Lead (Pb)": 11.34,
    "Cadmium (Cd)": 8.65,
    "Mercury (Hg)": 13.534
}

safe_limits_ml = {
    "Lead (Pb)": 0.01,      # ml
    "Cadmium (Cd)": 0.003,
    "Mercury (Hg)": 0.001
}

# --- حساب عدد المولات والكتلة ---
def calculate_moles_mass_volume(v, metal_name):
    molar_mass = molar_masses[metal_name]  # g/mol
    density = densities[metal_name]        # g/cm³
    try:
        n = (2.2e9 * 1e-3 / (v**2) - 1) / (molar_mass * 1e-3)
        if n < 0:
            return None, None, None, "Error: Moles calculated as negative!"
        mass_mg = n * molar_mass * 1000  # mg
        volume_ml = (mass_mg / 1000) / density
        return n, mass_mg, volume_ml, ""
    except Exception as e:
        return None, None, None, str(e)

if v_input > 0:
    n, mass_mg, volume_ml, error = calculate_moles_mass_volume(v_input, metal)
    
    if error:
        st.error(error)
    else:
        # --- تحديد حالة الأمان ---
        if volume_ml > safe_limits_ml[metal]:
            status_text = "Unsafe for human use"
            status_color = "#FF4C4C"  # أحمر
        else:
            status_text = "Safe for human use"
            status_color = "#90EE90"  # أخضر فاتح

        # --- عرض النتائج في 3 مربعات ---
        col1, col2, col3 = st.columns(3)

        col1.markdown(f"""
        <div style='background-color:#ADD8E6; padding:15px; border-radius:10px; text-align:center;'>
            <h5 style='font-size:16px;'>Moles (n)</h5>
            <p style='font-size:14px;'>{n:.6f}</p>
        </div>
        """, unsafe_allow_html=True)

        col2.markdown(f"""
        <div style='background-color:#ADD8E6; padding:15px; border-radius:10px; text-align:center;'>
            <h5 style='font-size:16px;'>Mass (mg)</h5>
            <p style='font-size:14px;'>{mass_mg:.6f}</p>
            <h5 style='font-size:16px;'>Volume (ml)</h5>
            <p style='font-size:14px;'>{volume_ml:.6f}</p>
        </div>
        """, unsafe_allow_html=True)

        col3.markdown(f"""
        <div style='background-color:{status_color}; padding:15px; border-radius:10px; text-align:center;'>
            <h5 style='font-size:16px;'>Status</h5>
            <p style='font-size:14px;'>{status_text}</p>
        </div>
        """, unsafe_allow_html=True)

