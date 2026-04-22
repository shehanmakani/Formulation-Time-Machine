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
    half_life_months: float

class FormulationMachine:
    def __init__(self, name: str, temp_c: float = 25.0):
        self.name = name
        self.temp_k = temp_c + 273.15
        self.ingredients: List[Ingredient] = []

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
        scores = [math.exp(-(0.693/i.half_life_months) * months * eff_speed) for i in self.ingredients]
        avg = (sum(scores) / len(scores)) * 100 if scores else 100
        return {"month": months, "integrity_score": round(avg, 2)}
