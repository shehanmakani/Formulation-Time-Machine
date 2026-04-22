import matplotlib.pyplot as plt
import os

def generate_stability_chart(time_points, integrity_scores, product_name, filename="docs/stability_curve.png"):
    """
    Generates a professional-grade stability plot showing the decay of a formulation.
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    plt.style.use('ggplot')
    plt.figure(figsize=(10, 6))
    plt.plot(time_points, integrity_scores, color='#2c3e50', linewidth=2.5, marker='o', label="System Integrity %")
    plt.axhline(y=90, color='#e74c3c', linestyle='--', alpha=0.6, label="90% Potency Threshold")
    plt.title(f"Predictive Lifecycle Simulation: {product_name}", fontsize=14, fontweight='bold')
    plt.xlabel("Storage Time (Months)", fontsize=12)
    plt.ylabel("Overall Integrity Score", fontsize=12)
    plt.ylim(0, 105)
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    print(f"Chart saved successfully to {filename}")
