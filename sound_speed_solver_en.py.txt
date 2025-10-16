import streamlit as st
from sympy import symbols, Eq, solve, sqrt

# --- Page Setup ---
st.set_page_config(page_title="Sound Speed Solver", page_icon="🧮", layout="centered")

# --- Custom CSS for colors and style ---
st.markdown("""
    <style>
        body {
            background-color: #0b1d3a;
        }
        .main {
            background-color: #0b1d3a;
            color: #e0e0e0;
            font-family: 'Segoe UI', sans-serif;
        }
        h1, h2, h3, h4 {
            color: #FFD700; /* gold */
            text-align: center;
        }
        .stSelectbox, .stNumberInput, .stButton button {
            border-radius: 10px !important;
        }
        .stButton button {
            background: linear-gradient(90deg, #FFD700, #C0C0C0);
            color: black;
            border: none;
            font-weight: bold;
            transition: 0.3s;
        }
        .stButton button:hover {
            background: linear-gradient(90deg, #C0C0C0, #FFD700);
            color: black;
            transform: scale(1.05);
        }
        .result-card {
            background-color: #1a2f57;
            border: 1px solid #C0C0C0;
            border-radius: 15px;
            padding: 20px;
            color: #FFD700;
            font-size: 18px;
            text-align: center;
        }
        hr {
            border: 1px solid #C0C0C0;
        }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<h1>🔬 Sound Speed Solver</h1>", unsafe_allow_html=True)
st.markdown("""
<p style='text-align:center; color:#C0C0C0'>
An interactive scientific tool to calculate the number of moles (<b>n</b>) in a metal solution 
based on the speed of sound. Designed for ISEF scientific projects.
</p>
""", unsafe_allow_html=True)

# --- Constants ---
B = 2.2 * 10**9
one_over_1000 = 1 / 1000

# --- Element selection ---
element = st.selectbox("Select the element:", ["Cadmium (Cd)", "Mercury (Hg)", "Lead (Pb)"])

# --- Molar mass assignment ---
if "Cadmium" in element:
    M = 112.4
elif "Mercury" in element:
    M = 200.59
else:
    M = 207.2

st.markdown(f"<p style='color:#FFD700'>Molar Mass (M): {M} g/mol</p>", unsafe_allow_html=True)

# --- Input: measured speed ---
v_value = st.number_input("Enter the measured speed of sound (m/s):", min_value=0.0, value=1400.0, step=0.1)

# --- Equation setup ---
n = symbols('n')
eq = Eq(v_value, sqrt((B * one_over_1000) / ((n * M * one_over_1000) + 1)))

# --- Solve Button ---
if st.button("🔍 Calculate Number of Moles (n)"):
    try:
        solution = solve(eq, n)
        if solution:
            n_value = float(solution[0])
            st.markdown(f"<div class='result-card'>✅ Number of moles (n) = {n_value:.6f}</div>", unsafe_allow_html=True)
        else:
            st.warning("⚠️ No valid solution found.")
    except Exception as e:
        st.error(f"Error while solving: {e}")

st.markdown("<hr>", unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
<p style='text-align:center; color:#C0C0C0'>
Developed with ❤️ using <b>SymPy</b> + <b>Streamlit</b> <br>
© 2025 ISEF Project
</p>
""", unsafe_allow_html=True)
