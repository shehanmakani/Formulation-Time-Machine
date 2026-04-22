import matplotlib.pyplot as plt
def generate_chart(months, scores, filename="docs/stability_chart.png"):
    plt.figure(figsize=(8,4))
    plt.plot(months, scores, color='blue', marker='o')
    plt.title("Formulation Stability Curve")
    plt.xlabel("Months")
    plt.ylabel("Integrity %")
    plt.grid(True)
    plt.savefig(filename)
