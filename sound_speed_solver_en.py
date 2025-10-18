import streamlit as st
import math

# إعدادات الصفحة
st.set_page_config(
    page_title="Aguamenti Calculator",
    page_icon="🌊",
    layout="centered"
)

# تصميم الخلفية والألوان
st.markdown("""
    <style>
    body {
        background-color: #cfe8ff;
        color: #000000;
    }
    .main {
        background-color: #cfe8ff;
    }
    h1 {
        text-align: center;
        font-size: 3em;
        color: #ffffff;
        text-shadow: 0px 0px 10px #ffeb99;
        border-bottom: 3px solid #ffeb99;
        padding-bottom: 10px;
    }
    .stButton>button {
        background-color: #ffeb99;
        color: #000;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #fff6cc;
        color: #000;
    }
    .result-box {
        background-color: #ffeb99;
        color: #000000;
        font-weight: bold;
        text-align: center;
        border-radius: 15px;
        padding: 15px;
        margin-top: 20px;
        box-shadow: 0px 0px 10px #ffe97f;
    }
    </style>
""", unsafe_allow_html=True)

# العنوان والوصف
st.markdown("<h1>Aguamenti Calculator</h1>", unsafe_allow_html=True)
st.write("Use this calculator to find the number of moles (n) and total mass of your chosen heavy metal using your experimental sound speed.")

# اختيار العنصر
element = st.selectbox("Choose the heavy metal:", ["Cadmium (Cd)", "Mercury (Hg)", "Lead (Pb)"])

# قيم الكتل المولية
molar_masses = {
    "Cadmium (Cd)": 112.4,
    "Mercury (Hg)": 200.59,
    "Lead (Pb)": 207.2
}

# إدخال السرعة
v = st.number_input("Enter the calculated sound speed (m/s):", min_value=0.0, format="%.3f")

# عند الضغط على الزر
if st.button("Calculate moles (n) and mass"):
    try:
        M = molar_masses[element]
        numerator = (2.2 * 10**9) * (1 / 10**3)

        if v > 0:
            # حساب عدد المولات
            n = ((numerator / (v**2)) - 1) / (M * (1/10**3))
            n = max(n, 0)  # منع النتائج السالبة

            # حساب الكتلة الكلية
            mass = n * M

            # عرض النتائج في مربعين منفصلين
            st.markdown(
                f"""
                <div class='result-box'>
                    The number of moles (n) for <b>{element}</b> is:<br>
                    <span style='font-size:22px;'>{n:.4f} mol</span>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div class='result-box'>
                    The total mass is:<br>
                    <span style='font-size:22px;'>{mass:.4f} g</span>
                </div>
                """,
                unsafe_allow_html=True
            )

        else:
            st.warning("Please enter a valid (non-zero) speed value.")
    except Exception as e:
        st.error(f"Error: {e}")

