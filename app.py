import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math

class Ingredient:
    def __init__(self, name, function, percentage, reactivity, half_life_months):
        self.name = name
        self.function = function
        self.percentage = percentage
        self.reactivity = reactivity
        self.half_life_months = half_life_months

class FormulationMachine:
    def __init__(self, name, temp_c):
        self.name = name
        self.temp_k = temp_c + 273.15
        self.ingredients = []
    def add_ingredient(self, ing): 
        self.ingredients.append(ing)
    def _get_accel(self): 
        return 2.0 ** ((self.temp_k - 298.15) / 10.0)
    def predict_state(self, months):
        accel = self._get_accel()
        eff = months * accel
        score = 100.0
        for ing in self.ingredients:
            k = math.log(2) / ing.half_life_months
            rem = math.exp(-k * eff)
            score -= ((1 - rem) * ing.reactivity * 100)
        return {"integrity": max(0, round(score, 2)), "accel": round(accel, 2)}

# --- UI SETUP ---
st.set_page_config(page_title="Formulation Time Machine", layout="wide")
st.title("🧪 Formulation Time Machine")
st.markdown("---")

# Sidebar
st.sidebar.header("Control Panel")
temp = st.sidebar.slider("Storage Temperature (°C)", 20, 50, 25)
duration = st.sidebar.slider("Duration (Months)", 1, 24, 12)
use_synergy = st.sidebar.checkbox("Apply Synergy (Ferulic Acid)", value=True)

# Calculation - FIXING THE ARGUMENT COUNT HERE
machine = FormulationMachine("Simulation", temp)
machine.add_ingredient(Ingredient("L-Ascorbic Acid", "Active", 15.0, 0.95, 3.0))
if use_synergy:
    machine.add_ingredient(Ingredient("Ferulic Acid", "Stabilizer", 0.5, 0.1, 24.0))

# Data Generation
report_months = [0, 1, 3, 6, 12, 24]
results = [machine.predict_state(m) for m in report_months]
accel_factor = results[0]['accel']

# Layout
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Stability Projection")
    months_plot = list(range(0, duration + 1))
    scores_plot = [machine.predict_state(m)["integrity"] for m in months_plot]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(months_plot, scores_plot, color='#1f77b4', linewidth=3)
    ax.fill_between(months_plot, scores_plot, alpha=0.2)
    ax.set_ylim(0, 105)
    ax.set_ylabel("Integrity (%)")
    ax.set_xlabel("Time (Months)")
    st.pyplot(fig)

with col2:
    st.subheader("Generated Report Data")
    df = pd.DataFrame({
        "Month": report_months,
        "Integrity (%)": [r['integrity'] for r in results]
    })
    st.table(df)
    st.metric("Thermal Acceleration Factor", f"{accel_factor}x")

st.markdown("---")
st.subheader("Academic Context & Methodology")
st.latex(r"C(t) = C_0 e^{-kt} \cdot 2^{\frac{T - 25}{10}}")
st.info("This simulation utilizes pseudo-first-order kinetics combined with the Arrhenius equation.")

report_text = f"Formulation Stability Report\nTemp: {temp}C\nAcceleration: {accel_factor}x\n\nResults:\n{df.to_string(index=False)}"
st.download_button("Download Report (.txt)", report_text, file_name="stability_report.txt")
