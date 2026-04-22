import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math

class Ingredient:
    def __init__(self, name, function, percentage, reactivity, half_life_months):
        self.name, self.function, self.percentage = name, function, percentage
        self.reactivity, self.half_life_months = reactivity, half_life_months

class FormulationMachine:
    def __init__(self, name, temp_c):
        self.name, self.temp_k = name, temp_c + 273.15
        self.ingredients = []
    def add_ingredient(self, ing): self.ingredients.append(ing)
    def _get_accel(self): return 2.0 ** ((self.temp_k - 298.15) / 10.0)
    def predict_state(self, months):
        accel = self._get_accel()
        eff = months * accel
        score = 100.0
        for ing in self.ingredients:
            k = math.log(2) / ing.half_life_months
            rem = math.exp(-k * eff)
            score -= ((1 - rem) * ing.reactivity * 100)
        return {"integrity": max(0, round(score, 2)), "accel": round(accel, 2)}

st.set_page_config(page_title="Formulation Time Machine", layout="wide")
st.title("🧪 Formulation Time Machine")

temp = st.sidebar.slider("Storage Temperature (°C)", 20, 50, 25)
duration = st.sidebar.slider("Duration (Months)", 1, 24, 12)
use_synergy = st.sidebar.checkbox("Apply Synergy", value=True)

machine = FormulationMachine("Simulation", temp)
machine.add_ingredient(Ingredient("L-Ascorbic Acid", "Active", 15.0, 0.95, 3.0))
if use_synergy:
    machine.add_ingredient(Ingredient("Ferulic Acid", "Stabilizer", 0.5, 0.1, 24.0))

months_plot = list(range(0, duration + 1))
scores_plot = [machine.predict_state(m)["integrity"] for m in months_plot]

fig, ax = plt.subplots()
ax.plot(months_plot, scores_plot, color='#1f77b4', linewidth=3)
ax.set_ylim(0, 105)
st.pyplot(fig)

st.subheader("Academic Context")
st.latex(r"C(t) = C_0 e^{-kt} \cdot 2^{\frac{T - 25}{10}}")
