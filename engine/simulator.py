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
        self.ingredients: List[Ingredient] = []

    def add_ingredient(self, ing: Ingredient):
        self.ingredients.append(ing)

    def _get_acceleration_factor(self):
        return 2.0 ** ((self.temp_k - 298.15) / 10.0)

    def predict_state(self, months: int) -> Dict:
        accel = self._get_acceleration_factor()
        eff_months = months * accel
        status = {"month": months, "integrity_score": 100.0, "alerts": [], "composition_drift": {}}
        for ing in self.ingredients:
            k = math.log(2) / ing.half_life_months
            remaining = math.exp(-k * eff_months)
            status["composition_drift"][ing.name] = round(ing.percentage * remaining, 3)
            status["integrity_score"] -= ((1 - remaining) * ing.reactivity * 100)
        status["integrity_score"] = max(0, round(status["integrity_score"], 2))
        return status
