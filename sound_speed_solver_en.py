import streamlit as st
import math
import base64

# إعداد الصفحة
st.set_page_config(
    page_title="Aguamenti Polluter Calculator",
    page_icon="wave_icon.svg",
    layout="centered"
)

# CSS لتصميم الخلفية الزرقاء الغامقة بحواف ذهبية والعنوان الذهبي
st.markdown(
    """
    <style>
        body {
            background-color: #0a1a3d;
            color: white;
        }
        .main {
            border: 4px solid gold;
            border-radius: 20px;
            padding: 40px;
            background-color: #0a1a3d;
            box-shadow: 0px 0px 25px rgba(255, 215, 0, 0.4);
        }
        h1 {
            color: gold;
            text-align: center;
            font-family: 'Trebuchet MS', sans-serif;
            font-size: 42px;
            text-shadow: 0px 0px 10px gold;
        }
        h3 {
            color: silver;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# العنوان والوصف
st.markdown("<h1>Aguamenti Polluter Calculator</h1>", unsafe_allow_html=True)
st.write("Welcome to Aguamenti Polluter Calculator! Use this calculator to determine the number of moles (n) and the total mass of the heavy metal you choose using the calculated sound speed in your experiment.")

# قائمة العناصر
elements = {
    "Cadmium (Cd)": 112.4,
    "Mercury (Hg)": 200.59,
    "Lead (Pb)": 207.2
}

element = st.selectbox("Select the element:", list(elements.keys()))
molar_mass = elements[element]

speed = st.number_input("Enter the calculated sound speed (m/s):", min_value=0.0, format="%.4f")

if st.button("Calculate"):
    try:
        # حساب عدد المولات
        n = ((math.sqrt(2.2e9 * (1/1e3)) / speed) - 1) / (molar_mass * (1/1e3))
        n = abs(n)  # منع القيم السالبة
        total_mass = n * molar_mass

        st.success(f"Number of moles (n): {n:.6f}")
        st.info(f"Total mass: {total_mass:.4f} g")

    except Exception as e:
        st.error(f"Error in calculation: {e}")

