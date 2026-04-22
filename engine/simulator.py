import math
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Ingredient:
    name: str
    function: str
    percentage: float
    reactivity: float
    volatility: float
    half_life_months: float = 24.0

class FormulationMachine:
    def __init__(self, name: str, temp_c: float = 25.0):
        self.name = name
        self.temp_k = temp_c + 273.15
        self.ingredients = []

    def add_ingredient(self, ing: Ingredient):
        self.ingredients.append(ing)

    def _get_stabilization_bonus(self):
        bonus = 1.0
        fns = [i.function for i in self.ingredients]
        if "Stabilizer" in fns: bonus *= 0.4
        if "Chelator" in fns: bonus *= 0.7
        return bonus

    def predict_state(self, months: int) -> Dict:
        accel = 2.0 ** ((self.temp_k - 298.15) / 10.0)
        eff_speed = accel * self._get_stabilization_bonus()
        
        status = {"month": months, "integrity_score": 100.0, "composition_drift": {}}
        total_degradation = 0
        for ing in self.ingredients:
            k = math.log(2) / ing.half_life_months
            remaining_ratio = math.exp(-k * months * eff_speed)
            status["composition_drift"][ing.name] = round(ing.percentage * remaining_ratio, 3)
            total_degradation += (1 - remaining_ratio) * ing.reactivity
            
        status["integrity_score"] = max(0, round(100 - (total_degradation * 100), 2))
        return status
