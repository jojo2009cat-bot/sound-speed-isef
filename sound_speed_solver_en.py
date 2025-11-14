import streamlit as st
import math

# -----------------------
# بيانات العناصر والحدود القصوى
# -----------------------
metals = {
    "Lead (Pb)": {"molar_mass": 207.2, "max_mass_mg": 0.01},
    "Cadmium (Cd)": {"molar_mass": 112.41, "max_mass_mg": 0.003},
    "Mercury (Hg)": {"molar_mass": 200.59, "max_mass_mg": 0.001},
}

# -----------------------
# تصميم الواجهة
# -----------------------
st.set_page_config(page_title="Aguamenti Calculator", page_icon="⚗️", layout="centered")
st.markdown(
    """
    <div style='text-align:center;'>
        <h1 style='color:#2a52be;'>Aguamenti Calculator for Heavy Metals</h1>
        <p style='color:#5f9ea0;'>A calculator that gives you the amount of heavy metals in fresh water using the velocity of sound</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<hr style='border:1px solid #f0e68c'>", unsafe_allow_html=True)

# -----------------------
# اختيار المعدن وإدخال السرعة
# -----------------------
metal_choice = st.selectbox("Choose the metal", list(metals.keys()))
v = st.number_input("Enter the velocity of sound (m/s)", min_value=0.0, format="%.5f")

# -----------------------
# الحسابات
# -----------------------
if v > 0:
    molar_mass = metals[metal_choice]["molar_mass"]  # g/mol
    max_mass_mg = metals[metal_choice]["max_mass_mg"]

    # معادلة حساب عدد المولات
    try:
        n = (2.2e9 * 1e-3) / (v**2) - 1
        n = n / (molar_mass * 1e-3)  # تحويل g/mol إلى kg/mol
        n = round(n, 6)
    except:
        n = -1

    if n < 0:
        st.error("Error: Number of moles calculated is negative.")
        n = 0

    # حساب الكتلة بالمللي جرام
    mass_mg = n * molar_mass * 1000  # g * 1000 = mg
    mass_mg = round(mass_mg, 6)
    
    # -----------------------
    # تحديد حالة الأمان
    # -----------------------
    if mass_mg > max_mass_mg:
        safety_status = ("Unsafe for human use", "#ff4c4c")
    else:
        safety_status = ("Safe for human use", "#90ee90")
    
    # -----------------------
    # عرض النتائج
    # -----------------------
    st.markdown(
        f"""
        <div style='display:flex; gap:20px; justify-content:center; margin-top:20px;'>
            <div style='background-color:#add8e6; padding:15px; border-radius:10px; text-align:center; width:180px;'>
                <h3>Number of Moles</h3>
                <p>{n}</p>
            </div>
            <div style='background-color:#add8e6; padding:15px; border-radius:10px; text-align:center; width:180px;'>
                <h3>Mass (mg)</h3>
                <p>{mass_mg}</p>
                <small>Maximum allowed: {max_mass_mg} mg</small>
            </div>
            <div style='background-color:{safety_status[1]}; padding:15px; border-radius:10px; text-align:center; width:180px;'>
                <h3>Safety Status</h3>
                <p>{safety_status[0]}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.warning("Please enter a velocity greater than zero.")

