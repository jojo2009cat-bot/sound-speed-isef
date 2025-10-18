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
        background-color: #0b1e3d;
        color: white;
    }
    .main {
        background-color: #0b1e3d;
    }
    h1 {
        text-align: center;
        font-size: 3em;
        color: white;
        text-shadow: 0px 0px 10px gold, 0px 0px 20px gold;
        border-bottom: 3px solid gold;
        padding-bottom: 10px;
    }
    .stButton>button {
        background-color: gold;
        color: black;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #ffea75;
        color: black;
    }
    .result-box {
        background-color: gold;
        color: white;
        font-weight: bold;
        text-align: center;
        border-radius: 15px;
        padding: 15px;
        margin-top: 20px;
        box-shadow: 0px 0px 15px gold;
    }
    </style>
""", unsafe_allow_html=True)

# العنوان والوصف
st.markdown("<h1>Aguamenti Calculator</h1>", unsafe_allow_html=True)
st.write("Use this calculator to find the number of moles (n) of your chosen heavy metal based on your calculated sound speed (v).")

# اختيار العنصر
element = st.selectbox("Choose the heavy metal:", ["Cadmium (Cd)", "Mercury (Hg)", "Lead (Pb)"])

# قيم الكتل المولية للعناصر
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
            # حساب عدد المولات n
            n = ((numerator / (v**2)) - 1) / (M * (1/10**3))
            n = max(n, 0)  # منع النتائج السالبة

            # حساب الكتلة الكلية
            mass = n * M

            # عرض النتائج داخل مربع ذهبي
            st.markdown(
                f"""
                <div class='result-box'>
                    The number of moles (n) for <b>{element}</b> is:<br>
                    <span style='font-size:22px;'>{n:.4f} mol</span><br><br>
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
