import streamlit as st

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

safe_limits_mg = {
    "Lead (Pb)": 0.01,      # mg
    "Cadmium (Cd)": 0.003,
    "Mercury (Hg)": 0.001
}

# --- حساب عدد المولات والكتلة ---
def calculate_moles_and_mass(v, metal_name):
    molar_mass = molar_masses[metal_name]  # g/mol
    try:
        numerator = 2.2e6
        denominator = v**2
        n = (numerator / denominator - 1) / (molar_mass * 1e-3)
        # إذا n < 0 فهذا خطأ، أما n = 0 طبيعي
        if n < 0:
            return None, None, "Error: Moles calculated as negative!"
        mass_mg = n * molar_mass * 1000  # mg
        return n, mass_mg, ""
    except Exception as e:
        return None, None, str(e)

if v_input > 0:
    n, mass_mg, error = calculate_moles_and_mass(v_input, metal)
    
    if error:
        st.error(error)
    else:
        # --- تحديد حالة الأمان بناءً على الكتلة بالملليجرام ---
        if mass_mg > safe_limits_mg[metal] + 1e-9:
            status_text = "Unsafe for human use"
            status_color = "#FF4C4C"  # أحمر
        else:
            status_text = "Safe for human use"
            status_color = "#90EE90"  # أخضر فاتح

        # --- عرض النتائج ---
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
        </div>
        """, unsafe_allow_html=True)

        col3.markdown(f"""
        <div style='background-color:{status_color}; padding:15px; border-radius:10px; text-align:center;'>
            <h5 style='font-size:16px;'>Status</h5>
            <p style='font-size:14px;'>{status_text}</p>
        </div>
        """, unsafe_allow_html=True)
