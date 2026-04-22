from engine.simulator import FormulationMachine, Ingredient
from data.chemicals import CHEMICAL_PROPERTIES
from engine.visualizer import generate_stability_chart

def run():
    formula = {"L-Ascorbic Acid": 15.0, "Ferulic Acid": 0.5, "Water": 83.5, "Phenoxyethanol": 1.0}
    machine = FormulationMachine("C-Serum-Visualized", temp_c=40.0)
    for name, pct in formula.items():
        p = CHEMICAL_PROPERTIES.get(name, {"reactivity": 0.1, "volatility": 0.1, "half_life": 24.0, "function": "Misc"})
        machine.add_ingredient(Ingredient(name, p["function"], pct, p["reactivity"], p["volatility"], p["half_life"]))
    
    months = list(range(0, 25))
    scores = [machine.predict_state(m)["integrity_score"] for m in months]
    
    print("--- Running Simulation & Generating Chart ---")
    print(f"Month 24 Integrity: {scores[-1]}%")
    generate_stability_chart(months, scores, machine.name)

if __name__ == "__main__":
    run()
