# SGCV/ALP/KM Comparison
## Project Codename "Condor"

A unified simulation and analysis framework comparing three dark photon production models:

- **SGCV**: Superluminal Graviton Condensate Vacuum  
- **ALP**: Axion-Like Particle scenario  
- **KM**: Kaluza–Klein photon excitations  
---
It includes Monte Carlo event generation for Higgs → γγ + γ′ decays, simplified detector geometry (ATLAS/SHiP-like), and visualization tools for analyzing spatial and temporal displacement (Δx vs Δt) distributions.

## 🚀 Launch on Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Galactic-Code-Developers/SGCV_ALP_KM_Comparison/blob/main/SGCV_ALP_KM_Comparison_v1.1_post_geom.ipynb)

---

## 📁 Project Structure

```
SGCV_ALP_KM_Comparison/
│
├── SGCV_ALP_KM_Comparison_v1.1_post_geom.ipynb  # ✔ Updated Colab notebook
├── SGCV_ALP_KM_Comparison_v_e31ca7f9.ipynb      # Colab notebook
├── main_simulation_runner.py                    # Main orchestrator
├── sgcv_simulation.py                           # SGCV model
├── alp_simulation.py                            # ALP model
├── km_simulation.py                             # Kaluza–Klein model
├── event_generator.py                           # Higgs → γγ + γ′ event generator
├── plot_utils.py                                # Plotting functions
├── detector_geometry.gdml                       # Detector geometry file
├── detector_geometry_layered.gdml               # ✔ Layered detector (tracker + ECAL + HCAL)
├── requirements.txt                             # Python dependencies
├── __init__.py                                  # Package initializer
├── LICENSE                                      # (MIT )
└── README.md                                    # Project description
```

---

## 🔧 Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/Galactic-Code-Developers/SGCV_ALP_KM_Comparison.git
cd SGCV_ALP_KM_Comparison
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the simulation from the notebook or terminal:

```bash
python main_simulation_runner.py
```

---

## 📊 Output

- Δx vs Δt scatter plots  
- Overlaid histograms for SGCV, ALP, and KM  
- Model comparison visuals for publication and export

---

## 📄 License

MIT License

Copyright (c) 2025 Kapodistrian Academy of Science
