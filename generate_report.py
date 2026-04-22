import os
import math

# Attempt to import your local engine, fallback to basic logic if path is tricky
try:
    from engine.simulator import FormulationMachine, Ingredient
except ImportError:
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

def get_report_data():
    months = [0, 1, 3, 6, 12, 24]
    cheap = FormulationMachine("Standard", 40.0)
    cheap.add_ingredient(Ingredient("L-Ascorbic Acid", "Active", 15.0, 0.95, 0.0, 3.0))
    c_scores = [cheap.predict_state(m)["integrity_score"] for m in months]
    opt = FormulationMachine("Stabilized", 40.0)
    opt.add_ingredient(Ingredient("L-Ascorbic Acid", "Active", 15.0, 0.95, 0.0, 3.0))
    opt.add_ingredient(Ingredient("Ferulic Acid", "Stabilizer", 0.5, 0.1, 0.0, 24.0))
    opt_scores = [opt.predict_state(m)["integrity_score"] for m in months]
    return months, c_scores, opt_scores

months, cheap, opt = get_report_data()
latex_content = r"""
\documentclass[11pt,a4paper]{article}
\usepackage{amsmath}
\usepackage{booktabs}
\usepackage{geometry}
\geometry{margin=1in}
\title{Predictive Kinetic Modeling of L-Ascorbic Acid Stability}
\author{Shehan Makani \\ \small Formulation Time Machine Project}
\date{\today}
\begin{document}
\maketitle
\section{Results (Accelerated 40$^{\circ}$C)}
\begin{table}[h]
\centering
\begin{tabular}{lcccccc}
\toprule
Month & 0 & 1 & 3 & 6 & 12 & 24 \\ \midrule
Standard (\%) & """ + f"{cheap[0]} & {cheap[1]} & {cheap[2]} & {cheap[3]} & {cheap[4]} & {cheap[5]}" + r""" \\ 
Stabilized (\%) & """ + f"{opt[0]} & {opt[1]} & {opt[2]} & {opt[3]} & {opt[4]} & {opt[5]}" + r""" \\ \bottomrule
\end{tabular}
\end{table}
\end{document}
"""
os.makedirs("docs", exist_ok=True)
with open("docs/stability_report.tex", "w") as f:
    f.write(latex_content)
print("Success: docs/stability_report.tex generated.")
