# 🧪 Formulation Time Machine
**Predictive Kinetic Modeling for Dermatological Stability**

The **Formulation Time Machine** is a computational tool designed to simulate the shelf-life and molecular integrity of L-Ascorbic Acid (Vitamin C) under varying thermal conditions. By blending the **Arrhenius Equation** with **First-Order Kinetics**, this app provides formulators with a "Digital Twin" to stress-test their antioxidant networks.

## 🚀 Live Demo
[View the Live Web App on Streamlit](https://formulation-time-machine.streamlit.app/)

## 🧬 Scientific Methodology

### 1. Thermal Acceleration
The engine utilizes the Arrhenius-derived $Q_{10}$ coefficient to model thermal stress. For every 10°C increase in storage temperature, the reaction rate effectively doubles:
$$k = A e^{-E_a / RT} \approx 2^{\frac{T_{storage} - 25}{10}}$$

### 2. Degradation Kinetics
Molecular decay is modeled as a pseudo-first-order reaction, where integrity ($C$) is a function of time ($t$) and the specific decay constant ($k$):
$$C(t) = C_0 e^{-kt}$$

### 3. Synergistic Stabilization
The model accounts for **Antioxidant Cascades**. By introducing Ferulic Acid as a stabilizer, the engine reduces the effective reactivity of the system, simulating the "regeneration" of Vitamin C molecules.

## 📂 Project Architecture
- **app.py**: The main Streamlit dashboard.
- **engine/**: Simulation and visualization logic.
- **data/**: Chemical constant database.

## 👨‍🔬 Author
**Shehan Makani**
