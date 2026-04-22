from engine.simulator import FormulationMachine, Ingredient
from data.chemicals import CHEMICAL_PROPERTIES
import os

def run():
    formula = {"L-Ascorbic Acid": 15.0, "Water": 84.0, "Phenoxyethanol": 1.0}
    machine = FormulationMachine("C-Serum-v1", temp_c=40.0)
    for name, pct in formula.items():
        p = CHEMICAL_PROPERTIES.get(name)
        machine.add_ingredient(Ingredient(name, p["function"], pct, p["reactivity"], p["volatility"], p["half_life"]))
    
    print("Simulation complete. Check results in main output.")
    for m in [1, 6, 12, 24]:
        res = machine.predict_state(m)
        print(f"Month {m}: Integrity {res['integrity_score']}%")

if __name__ == "__main__":
    run()
