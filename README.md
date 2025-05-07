# SGCV/ALP/KM Comparison
## Project Codename "Condor"

A unified simulation and analysis framework comparing three dark photon production models:

- **SGCV**: Superluminal Graviton Condensate Vacuum  
- **ALP**: Axion-Like Particle scenario  
- **KM**: Kaluza–Klein photon excitations  

---

## 📁 Project Structure

```
SGCV_ALP_KM_Comparison/
│
├── SGCV_ALP_KM_Comparison_v_e31ca7f9.ipynb     # Colab notebook
├── main_simulation_runner.py                  # Main orchestrator
├── sgcv_simulation.py                         # SGCV model
├── alp_simulation.py                          # ALP model
├── km_simulation.py                           # Kaluza–Klein model
├── event_generator.py                         # Higgs → γγ + γ′ event generator
├── plot_utils.py                              # Plotting functions
├── detector_geometry.gdml                     # Detector geometry file
├── requirements.txt                           # Python dependencies
├── __init__.py                                # Package initializer
├── LICENSE                                    # (Optional: MIT / GPL)
└── README.md                                  # Project description
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

MIT or GPL — choose based on your publication needs.
