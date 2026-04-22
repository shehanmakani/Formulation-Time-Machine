import matplotlib.pyplot as plt
import os

def generate_comparison_chart(months, data_dict, filename="docs/stress_test_comparison.png"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    plt.style.use('bmh')
    plt.figure(figsize=(12, 7))
    colors = ['#e74c3c', '#27ae60'] 
    for (label, scores), color in zip(data_dict.items(), colors):
        plt.plot(months, scores, label=label, color=color, linewidth=3, marker='o')
    plt.axhline(y=90, color='black', linestyle='--', alpha=0.3)
    plt.title("Stress Test: Standard Formula vs. Optimized Synergy", fontsize=15, pad=20)
    plt.xlabel("Months at 40°C (Accelerated)", fontsize=12)
    plt.ylabel("System Integrity (%)", fontsize=12)
    plt.ylim(0, 105)
    plt.legend(facecolor='white', frameon=True)
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    print(f"Comparison chart saved to {filename}")
