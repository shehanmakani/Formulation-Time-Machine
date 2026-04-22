import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math

class Ingredient:
    def __init__(self, name, function, percentage, reactivity, volatility, half_life_months):
        self.name, self.function, self.percentage = name, function, percentage
        self.reactivity, self.volatility, self.half_life_months = reactivity, volatility, half_life_months

class FormulationMachine:
    def __init__(self, name, temp_c):
        self.name = name
        self.temp_k = temp_c + 273.15
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
        return {"integrity_score": max(0, round(score, 2))}

st.set_page_config(page_title="Formulation Time Machine", page_icon="🧪")
st.title("🧪 Formulation Time Machine")

temp = st.sidebar.slider("Storage Temperature (°C)", 20, 50, 40)
duration = st.sidebar.slider("Months", 1, 24, 12)
use_synergy = st.sidebar.checkbox("Apply Synergy (Ferulic + Phytic)", value=True)

machine = FormulationMachine("Sim", temp)
machine.add_ingredient(Ingredient("L-Ascorbic Acid", "Active", 15.0, 0.95, 0.0, 3.0))
if use_synergy:
    machine.add_ingredient(Ingredient("Ferulic Acid", "Stab", 0.5, 0.1, 0.0, 24.0))

months = list(range(0, duration + 1))
scores = [machine.predict_state(m)["integrity_score"] for m in months]

st.metric("Final Integrity", f"{scores[-1]}%")
fig, ax = plt.subplots()
ax.plot(months, scores, color='green' if use_synergy else 'red')
ax.set_ylim(0, 105)
st.pyplot(fig)
