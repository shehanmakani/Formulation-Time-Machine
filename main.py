from engine.simulator import FormulationMachine, Ingredient
from data.chemicals import CHEMICAL_PROPERTIES
from engine.visualizer import generate_comparison_chart

def run_stress_test():
    months = list(range(0, 25))
    results = {}
    
    # Cheap Formula
    cheap = FormulationMachine("Cheap Serum", temp_c=40.0)
    cheap.add_ingredient(Ingredient("L-Ascorbic Acid", "Active", 15.0, 0.95, 0.0, 3.0))
    cheap.add_ingredient(Ingredient("Water", "Solvent", 85.0, 0.0, 0.8, 999.0))
    
    # Optimized Formula
    opt = FormulationMachine("Optimized Serum", temp_c=40.0)
    opt.add_ingredient(Ingredient("L-Ascorbic Acid", "Active", 15.0, 0.95, 0.0, 3.0))
    opt.add_ingredient(Ingredient("Ferulic Acid", "Stabilizer", 0.5, 0.1, 0.0, 24.0))
    opt.add_ingredient(Ingredient("Phytic Acid", "Chelator", 0.5, 0.05, 0.0, 48.0))
    opt.add_ingredient(Ingredient("Water", "Solvent", 84.0, 0.0, 0.8, 999.0))

    results["Cheap Formula"] = [cheap.predict_state(m)["integrity_score"] for m in months]
    results["Optimized Formula"] = [opt.predict_state(m)["integrity_score"] for m in months]

    print(f"--- Comparison Month 12 ---")
    print(f"Cheap: {results['Cheap Formula'][12]}% | Optimized: {results['Optimized Formula'][12]}%")
    generate_comparison_chart(months, results)

if __name__ == "__main__":
    run_stress_test()
